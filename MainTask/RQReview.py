from typing import Dict

import fitz
import re


def _countSentences(text):
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return len(sentences)


def _countWords(text):
    words = text.split()
    return len(words)


def _countReferences(text):
    reference_pattern = re.compile(r'\[\d+, p\. \d+]')
    references = re.findall(reference_pattern, text)
    return len(references)


class PDF:
    text = str()
    lowText = str()
    questions = {}

    def __init__(self, pathToFile):
        doc = fitz.open(pathToFile)
        paragraphs = []
        current_paragraph = ""

        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            blocks = page.get_text("dict")["blocks"]
            previous_y = None
            for block in blocks:
                for line in block["lines"]:
                    line_text = " ".join([span["text"] for span in line["spans"]])
                    current_y = line["bbox"][1]
                    current_x = line["bbox"][0]

                    if (previous_y is not None and abs(current_y - previous_y) > 22) or (previous_y is not None and current_x > 119):
                        if current_paragraph:
                            paragraphs.append(current_paragraph.strip())
                        current_paragraph = line_text
                    else:
                        current_paragraph += " " + line_text

                    previous_y = current_y

            if current_paragraph:
                paragraphs.append(current_paragraph.strip())

        self.text = '\n'.join(paragraphs)
        self.lowText = self.text.lower()

    def delCol(self) -> None:  # delete collision
        try:
            self.text = self.text.replace('  ', ' ')
            self.text = self.text.replace('   ', ' ')
            self.text = self.text.replace('( ', '(')
            self.text = self.text.replace(' )', ')')
            self.text = self.text.replace('[ ', '[')
            self.text = self.text.replace(' ]', ']')
            self.text = self.text.replace(' .', '.')
        except Exception as e:
            print(e)

    def parsingQuestions(self):
        question_pattern = re.compile(r"(?i)(q\d+\..*?)\n", re.S)
        questions = re.findall(question_pattern, self.text)

        answers = []
        start_idx = 0

        for question in questions:
            question_idx = self.text.find(question, start_idx)

            next_question_match = re.search(r"(?i)(q\d+\..*?)\n", self.text[question_idx + len(question):])

            if next_question_match:
                next_question_idx = question_idx + len(question) + next_question_match.start()
            else:
                next_question_idx = len(self.text)

            answer = self.text[question_idx + len(question):next_question_idx].strip()
            answers.append(answer)

            start_idx = next_question_idx

        self.questions = dict(zip(questions, answers))
        print(self.questions)


class PDFChecker:
    def checkEv(self, PDFFile: PDF) -> str:

        CheckRef = self._checkReferences(PDFFile.lowText)
        CheckNumRef = self._checkLinksToReferences(PDFFile.questions)
        return CheckRef + '\n' + CheckNumRef

    def _checkReferences(self, PDFTextLow: str) -> str:  # checking references exist
        lenText = len(PDFTextLow)
        indexRef = PDFTextLow.rfind('\nreferences')
        if indexRef != -1:
            if lenText - indexRef > 10:
                return '✅ References on site'
            else:
                return '⚠️ Check the References'
        else:
            return '⛔ May be you have not the References'

    def _checkLinksToReferences(self, Questions: Dict[str, str]) -> str:  # checking count of the links
        res = ''

        for question in Questions.keys():
            refCount = _countReferences(Questions[question])
            wordCount = _countWords(Questions[question])
            sentencesCount = _countSentences(Questions[question])
            if refCount == 0:
                res += f'⛔ {question}\nYou forgot to specify the reference numbers for this question!\n'
            elif sentencesCount / refCount > 2:
                res += (
                    f'⚠️ {question}\nCheck again for links to the references in this question\nNumber of sentences: '
                    f'{sentencesCount}\nNumber of links: {refCount}\n')
            else:
                res += f'✅ {question}\nI think the links are enough\n'

        return res
