from .PDFFile import PDF

import google.generativeai as genai
import os

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


class QuestionsChecker:
    _RQ: PDF

    def __init__(self, RQ: PDF):
        self._RQ = RQ
        genai.configure(api_key=GOOGLE_API_KEY)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def check_the_correct(self):
        question = (f"You are an extremely picky teacher with years of experience in the "
                    f"Software Engineering field. Your task is to analyze papers of your "
                    f"students.\nPapers are given in form of pairs of question and the "
                    f"answer to that question.You always stick to the facts in the sources "
                    f"provided, and never make up new facts. There is the "
                    f"References {self._RQ.references}."
                    f"\nCommon mistakes that students make are: irrelevant to a question, "
                    f"irrational, has assumptions, has no example, sources, used in answer, "
                    f"are not referenced.\nFor all the answers stated below, inspect, "
                    f"whether they have any of the listed mistakes:")

        for q in self._RQ.questions.keys():
            question += f'{q}:{self._RQ.questions[q]}\n'

        question += ("your answer must be like this template: Q{question_number}: your assessment. "
                     "don't use any formatting")

        response = self.model.generate_content(question)

        response = response.text.split('\n')

        return response
