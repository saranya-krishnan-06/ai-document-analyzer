from PyPDF2 import PdfReader
from docx import Document
from fastapi import UploadFile


def extract_text_from_file(file: UploadFile):

    filename = file.filename.lower()

    if filename.endswith(".pdf"):
        reader = PdfReader(file.file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

    elif filename.endswith(".docx"):
        doc = Document(file.file)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text

    elif filename.endswith(".txt"):
        return file.file.read().decode("utf-8")

    else:
        raise ValueError("Unsupported file type")