#app/routes/analyze.py

from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel, Field
from app.services.ai_service import summarize_text, extract_keywords, analyze_sentiment
from app.services.file_service import extract_text_from_file
#from app.services.vector_store import add_documents
from app.utils.text_chunker import split_text
from app.services.vector_store import search
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
    
    #chunks = split_text(text)
    #add_documents(chunks)
    
    summary = summarize_text(text)
    sentiment = analyze_sentiment(text)
    keywords = extract_keywords(text)

    return {
        "summary": summary,
        "sentiment": sentiment,
        "keywords": keywords
    }
