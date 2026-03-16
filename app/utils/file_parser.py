from docx import Document
from pypdf import PdfReader


def extract_text_from_txt(file):
    return file.read().decode("utf-8")


def extract_text_from_docx(file):
    doc = Document(file)
    return "\n".join([p.text for p in doc.paragraphs])


def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text