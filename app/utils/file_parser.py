# app/utils/file_parser.py
from docx import Document
from pypdf import PdfReader


def extract_text_from_txt(file) -> str:
    return file.read().decode("utf-8")


def extract_text_from_docx(file) -> str:
    doc = Document(file)
    return "\n".join([p.text for p in doc.paragraphs if p.text.strip()])


def extract_text_from_pdf(file) -> str:
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted
    return text