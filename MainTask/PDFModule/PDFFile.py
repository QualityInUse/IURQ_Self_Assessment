import fitz
import re


class PDF:
    RQNum = int()
    text = str()
    lowText = str()
    questions = {}
    references = str()

    def __init__(self, pathToFile: str, RQNum: int):

        self.RQNum = RQNum

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

                    if previous_y is not None and abs(current_y - previous_y) > 14:
                        if current_paragraph:
                            paragraphs.append(current_paragraph.strip())
                        current_paragraph = line_text
                    else:
                        if current_paragraph and current_paragraph[-1] == '-':
                            current_paragraph = current_paragraph[:-1] + line_text
                        else:
                            current_paragraph += ' ' + line_text

                    previous_y = current_y

            if current_paragraph:
                paragraphs.append(current_paragraph.strip())

        self.text = '\n'.join(paragraphs)
        self.references = self.text[self.text.rfind('References'):]
        self.text = self.text[:self.text.rfind('References')]
        self.lowText = self.text.lower()

    def parsingQuestions(self):
        question_pattern = re.compile(r"(?i)(q\d+\.*.*?)\n", re.S)
        questions = re.findall(question_pattern, self.text)

        answers = []
        start_idx = 0

        for question in questions:
            question_idx = self.text.find(question, start_idx)

            next_question_match = re.search(r"(?i)(q\d+\.*.*?)\n", self.text[question_idx + len(question):])

            if next_question_match:
                next_question_idx = question_idx + len(question) + next_question_match.start()
            else:
                next_question_idx = len(self.text)

            answer = self.text[question_idx + len(question):next_question_idx].strip()
            answers.append(answer)

            start_idx = next_question_idx

        self.questions = dict(zip(questions, answers))
        print(self.questions)
