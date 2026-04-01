# app/services/document_chat_service.py
from app.services.vector_store import search
from app.services.ai_service import tokenizer, model
from app.core.logger import logger


def answer_question(question: str) -> str:
    """Search the document store and answer a question using flan-t5."""
    chunks = search(question, k=3)

    if not chunks:
        return "No documents have been uploaded yet. Please upload a file first using /analyze/file."

    context = " ".join(chunks)

    prompt = f"""Answer the question based on the context below.

Context:
{context}

Question:
{question}

Answer:"""

    logger.info(f"Answering question: {question}")
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
    outputs = model.generate(**inputs, max_new_tokens=100)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return answer