from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage


def create(file, data):
    template = DocxTemplate('files/report.docx')
    signature = 'files/acc.jpg'
    data['acc'] = InlineImage(template, signature, Cm(15))
    template.render(data)
    template.save(file)
