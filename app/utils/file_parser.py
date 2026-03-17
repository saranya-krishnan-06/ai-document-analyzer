#utils/file_parser.py
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

def extract_text_from_file(upload_file):

    filename = upload_file.filename.lower()

    if filename.endswith(".txt"):
        return extract_text_from_txt(upload_file.file)

    elif filename.endswith(".docx"):
        return extract_text_from_docx(upload_file.file)

    elif filename.endswith(".pdf"):
        return extract_text_from_pdf(upload_file.file)

    else:
        raise ValueError("Unsupported file type")