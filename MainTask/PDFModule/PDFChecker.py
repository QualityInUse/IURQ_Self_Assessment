from .PDFFile import PDF
from typing import Dict, List
import re
import os

from .QuestionsCheckerAI import QuestionsChecker


def _readQuestionsFromFile(pathToFile: str) -> List[str]:
    with open(pathToFile, 'r', encoding='utf-8') as file:
        questions = [line.strip() for line in file.readlines()]
    return questions


def _countSentences(text):
    sentences = re.split(r'(?<!\b\w\.\s)(?<!\b\w\.\w)(?<!\b\w\w\.)[.!?](?=\s+[A-Z])', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    print(sentences)
    return len(sentences)


def _countWords(text: str) -> int:
    words = text.split()
    return len(words)


def _countReferences(text: str) -> int:
    reference_pattern = re.compile(r'\[\d+, p\. \d+]|\[\d+, *pp. * \d+ *- *\d+]')
    references = re.findall(reference_pattern, text)
    return len(references)


def _countExample(text: str) -> int:
    example_pattern = re.compile(r"\(\b((ex\.)|(example)):\s+((\w+([,;:])?\s*.*)+)\)")
    examples = re.findall(example_pattern, text)

    return len(examples)


class PDFChecker:
    def checkEv(self, PDFFile: PDF) -> List[str]:

        CheckRef = self._checkReferences(PDFFile.lowText)
        CheckQuestions = self._checkQuestionsExist(PDFFile.questions, PDFFile.RQNum)

        questionFeedback = self._checkQuestions(PDFFile.questions)
        res = []

        questions = list(questionFeedback.keys())
        for i, question in enumerate(questions):
            if len(question) >= 4 and len(questions[i-1]) == 2:
                questionFeedback[questions[i-1]] = ''

        flag = False

        i = 0
        checkerQuestions = QuestionsChecker(PDFFile)
        response = checkerQuestions.check_the_correct()
        print(response)
        for question in questions:
            if len(question) >= 3 and flag:
                res[-1] += f'\n\n{question}{questionFeedback[question]}'
            else:
                res.append(f'{question}{questionFeedback[question]}{response[i]}')

            if len(question) == 2 and len(questionFeedback[question]) == 0:
                flag = True
            elif len(question) == 2 and len(questionFeedback[question]) != 0:
                flag = False

            i += 1

        res.append(f'Verification of RQ structure:\n{CheckRef}\n{CheckQuestions}')

        return res

    def _checkQuestionsExist(self, Questions: Dict[str, str], RQNum: int):
        path_to_questions = os.path.join(os.path.dirname(__file__), f'List_of_questions/{RQNum}.txt')
        questions = _readQuestionsFromFile(path_to_questions)
        for question in Questions.keys():
            q = " ".join(question.split(' ')[1:])
            if q in questions:
                questions.pop(questions.index(q))

        if not questions:
            return '✅ You have written all the questions'
        else:
            res = '\n'
            for question in questions:
                res += question + '\n'
            return f'⚠️ You may have forgotten to enter the following questions:{res}'

    def _checkQuestions(self, Questions: Dict[str, str]) -> Dict[str, str]:
        feedback = {}

        for question in Questions.keys():
            QPattern = re.compile("(?i)(Q\d+(\.*\d+)*)", re.S)
            QName = re.findall(QPattern, question)
            QName = QName[0][0].upper()
            feedReferences = self._checkLinksToReferences(Questions[question])

            feedback[QName] = f'\n\n{feedReferences}\n\n'

        return feedback

    def _checkExample(self, answer: str) -> str:  # checking example exist
        res = ''

        examples = _countExample(answer.lower())

        if examples:
            return f'✅ Examples on site'
        else:
            return f'⚠️ Check the Examples'

    def _checkReferences(self, references: str) -> str:  # checking references exist
        lenText = len(references)
        if lenText != 0:
            if lenText > 10:
                return '✅ The References part on site'
            else:
                return '⚠️ Check The References part'
        else:
            return '⛔ May be you have not The References part'

    def _checkLinksToReferences(self, answer: str) -> str:  # checking count of the links
        res = ''

        refCount = _countReferences(answer)
        sentencesCount = _countSentences(answer)
        exampleCount = _countExample(answer)

        if refCount == 0:
            res += (f'⛔ You forgot to specify the reference numbers for this question!\n'
                    f'(Every sentence that is not an example or your assumption should include reference)')
        elif sentencesCount - exampleCount > refCount:
            res += (
                f'⚠️ Check again for links to the references in this question\n'
                f'(Every sentence that is not an example or your assumption should include reference)\n'
                f'Number of sentences: '
                f'{sentencesCount - exampleCount}\nNumber of links: {refCount}\n')
        else:
            res += f'✅ I think the links are enough\n'

        return res
