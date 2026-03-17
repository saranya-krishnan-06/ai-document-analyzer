from fastapi import APIRouter
from pydantic import BaseModel
from app.services.document_chat_service import answer_question

router = APIRouter()


class QuestionRequest(BaseModel):
    question: str


@router.post("/chat")
def chat_with_document(request: QuestionRequest):
    answer = answer_question(request.question)

    return {
        "question": request.question,
        "answer": answer
    }