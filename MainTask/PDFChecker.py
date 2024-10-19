from PDFFile import PDF
from typing import Dict
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


class PDFChecker:
    def checkEv(self, PDFFile: PDF) -> str:

        CheckRef = self._checkReferences(PDFFile.lowText)
        CheckNumRef = self._checkLinksToReferences(PDFFile.questions)
        return CheckRef + '\n\n' + CheckNumRef

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
            sentencesCount = _countSentences(Questions[question])

            QPattern = re.compile("(?i)(Q\d+(\.*\d+)*)", re.S)

            QName = re.findall(QPattern, question)
            QName = QName[0][0].upper()

            if refCount == 0:
                res += f'⛔ {QName}\nYou forgot to specify the reference numbers for this question!\n'
            elif sentencesCount / refCount > 2:
                res += (
                    f'⚠️ {QName}\nCheck again for links to the references in this question\nNumber of sentences: '
                    f'{sentencesCount}\nNumber of links: {refCount}\n')
            else:
                res += f'✅ {QName}\nI think the links are enough\n'

        return res
