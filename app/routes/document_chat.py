# routes/document_chat.py
from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel

from app.services.document_chat_service import add_document_chunks, answer_question
from app.utils.text_chunker import split_text
from app.utils.file_parser import (
    extract_text_from_txt,
    extract_text_from_docx,
    extract_text_from_pdf,
)

router = APIRouter()


class QuestionRequest(BaseModel):
    question: str


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    filename = file.filename.lower()

    if filename.endswith(".txt"):
        text = extract_text_from_txt(file.file)
    elif filename.endswith(".docx"):
        text = extract_text_from_docx(file.file)
    elif filename.endswith(".pdf"):
        text = extract_text_from_pdf(file.file)
    else:
        return {"error": "Unsupported file type"}

    chunks = split_text(text)
    add_document_chunks(chunks)

    return {
        "message": "Document processed successfully",
        "chunks_added": len(chunks)
    }


@router.post("/chat")
def chat_with_document(request: QuestionRequest):
    answer = answer_question(request.question)

    return {
        "question": request.question,
        "answer": answer
    }