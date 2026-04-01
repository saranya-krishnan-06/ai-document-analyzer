# app/routes/analyze.py
from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel, Field
from app.services.ai_service import summarize_text, extract_keywords, analyze_sentiment
from app.services.vector_store import add_documents
from app.utils.text_chunker import split_text
from app.utils.file_parser import (
    extract_text_from_txt,
    extract_text_from_docx,
    extract_text_from_pdf,
)

router = APIRouter()


class TextRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=10,
        max_length=5000,
        description="Text must be between 10 and 5000 characters",
    )


@router.post("/file")
async def analyze_file(file: UploadFile = File(...)):
    filename = file.filename.lower()

    if filename.endswith(".txt"):
        text = extract_text_from_txt(file.file)
    elif filename.endswith(".docx"):
        text = extract_text_from_docx(file.file)
    elif filename.endswith(".pdf"):
        text = extract_text_from_pdf(file.file)
    else:
        raise HTTPException(status_code=400, detail="Unsupported file type. Use .txt, .docx, or .pdf")

    if not text.strip():
        raise HTTPException(status_code=422, detail="Could not extract any text from the file.")

    chunks = split_text(text)
    add_documents(chunks)

    summary = summarize_text(text)
    sentiment = analyze_sentiment(text)
    keywords = extract_keywords(text)

    return {
        "summary": summary,
        "sentiment": sentiment,
        "keywords": keywords,
        "chunks_indexed": len(chunks),
    }


@router.post("/summarize")
def summarize(request: TextRequest):
    result = summarize_text(request.text)
    return {"summary": result}


@router.post("/keywords")
def keywords(request: TextRequest):
    result = extract_keywords(request.text)
    return {"keywords": result}


@router.post("/sentiment")
def sentiment(request: TextRequest):
    result = analyze_sentiment(request.text)
    return {"sentiment": result}