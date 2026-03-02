from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ai_service import summarize_text, extract_keywords, analyze_sentiment

router = APIRouter()

class TextRequest(BaseModel):
    text: str

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