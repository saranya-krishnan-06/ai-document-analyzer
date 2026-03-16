from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel, Field
from app.services.ai_service import summarize_text, extract_keywords, analyze_sentiment
from app.services.file_service import extract_text_from_file
from app.utils.file_parser import (
    extract_text_from_txt,
    extract_text_from_docx,
    extract_text_from_pdf
)
router = APIRouter()
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
        return {"error": "Unsupported file type"}

    summary = summarize_text(text)
    sentiment = analyze_sentiment(text)
    keywords = extract_keywords(text)

    return {
        "summary": summary,
        "sentiment": sentiment,
        "keywords": keywords
    }
class TextRequest(BaseModel):
    text: str = Field(
        ..., 
        min_length=10,
        max_length=5000,
        description="Text must be between 10 and 5000 characters"
        )

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