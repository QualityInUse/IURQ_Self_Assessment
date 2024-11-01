import os
from iu_rq_self_assessment_bot.MainTask.PDFModule.PDFFile import PDF


PDF_FILE_PATH = os.path.join(os.path.dirname(__file__), 'Template (1).pdf')


def test_pdf_initialization():
    pdf = PDF(PDF_FILE_PATH, 1)
    print(pdf.text)
    assert pdf.text is not None
    assert pdf.lowText == pdf.text.lower()


def test_pdf_questions():
    pdf = PDF(PDF_FILE_PATH, 1)
    pdf.parsingQuestions()

    print(pdf.questions)
    questions = {
        'Q1 Tsui and Karam review questions': '',
        'Q1.1 Which decisions are those taken by the software engineer about the best ways '
        '(processes, techniques and technologies) to achieve the requirements?':
            'Your answer. (Ex.: apple, banana, etc) Your answer',
        'Q1.2 Define the depth versus the breadth issue in software complexity.': 'Your answer',
        'Q1.3 List two technical concerns in developing large systems.': 'Your answer',
        'Q1.4 What is meant by the term principles of software engineering?': 'Your answer',
        'Q2 Pressman': '',
        'Q2.1 Pressman discusses the problems of legacy software. What does he mean that'
        ' such software needs to be “re-engineered.” Give some specifics of re-engineering.': 'Your answer',
        'Q2.2 Pressman defines Software Engineering, so, what is the difference between '
        'Software Engineering and Computer Science?': 'Your answer (Example: one, two, three)',
        'Q2.3 Simply list the separate processes that a development team should manage. '
        'Also explain why each is, or is not important.': 'Your answer'
    }

    assert questions == pdf.questions
