from typing import Dict

import google.generativeai as genai
import os


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


class QuestionsChecker:

    _questions: Dict[str, str]

    def __init__(self, questions: Dict[str, str]):
        self._questions = questions
        genai.configure(api_key=GOOGLE_API_KEY)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def check_the_correct(self, question: str, answer: str):
        response = self.model.generate_content(f"Imagine that you are a very strict teacher who is paid to "
                                               f"find errors when checking assignments. Answer whether the student "
                                               f"answered the following question correctly or not. "
                                               f"If he answered incorrectly, indicate which part of the answer he "
                                               f"should revise. Question {question}: "
                                               f"Student answer: {answer}")
        print(response.text)
