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
                    f"answer to that question."
                    f"Be sure to check the presence of citations; I do a primary check for citation compliance with "
                    f"the following templates: [number_ref, p. number_page] or "
                    f"[number_ref, pp. number_page-number_page], if there are other links, indicate that "
                    f"they should be in this format. Check whether the answer completely covers the question, "
                    f"whether there are inconsistencies in it, check whether there is an example and whether this "
                    f"example matches the question.")

        for q in self._RQ.questions.keys():
            question += f'{q}:{self._RQ.questions[q]}\n'

        question += ("your answer must be like this template: AI Checking Q{question_number}: your assessment. "
                     "Don't use any formatting, just write your own review for each question presented. "
                     "your answer should look like this: "
                     "Q1: your assessment "
                     "... "
                     "Qn: your assessment ")

        response = self.model.generate_content(question)

        response = response.text.split('\n')

        while '' in response:
            response.remove("")

        return response
