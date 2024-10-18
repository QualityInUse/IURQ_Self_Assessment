import PyPDF2


class PDFChecker:
    def checkEv(self, PDFTextLow: str) -> str:
        CheckRef = self._checkReferences(PDFTextLow)

        return CheckRef

    def _checkReferences(self, PDFTextLow: str) -> str:
        lenText = len(PDFTextLow)
        indexRef = PDFTextLow.rfind('\nreferences')
        if indexRef != -1:
            if lenText - indexRef > 10:
                return '✅ References on site'
            else:
                return '⚠️ Check the References'
        else:
            return '⛔ May be you have not the References'


class PDF:
    text = str()
    lowText = str()

    def __init__(self, pathToFile):
        try:
            with open(pathToFile, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                for pageNum, page in enumerate(reader.pages):
                    self.text += page.extract_text() + '\n'
            self.lowText = self.text.lower()
        except Exception as e:
            print(e)

    def delCol(self) -> None:  # delete collision
        try:
            self.text = self.text.replace('  ', ' ')
            self.text = self.text.replace('( ', '(')
            self.text = self.text.replace(' )', ')')
            self.text = self.text.replace('[ ', '[')
            self.text = self.text.replace(' ]', ']')
            self.text = self.text.replace(' .', '.')
        except Exception as e:
            print(e)
