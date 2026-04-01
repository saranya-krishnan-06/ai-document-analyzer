# app/services/ai_service.py
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from app.core.config import settings
from app.core.logger import logger

# Load once at import time — shared across all services
tokenizer = AutoTokenizer.from_pretrained(settings.MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(settings.MODEL_NAME)

logger.info(f"Model loaded: {settings.MODEL_NAME}")


def summarize_text(text: str) -> str:
    try:
        logger.info("Summarizing text")
        prompt = f"Summarize the following text:\n\n{text}"
        inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
        outputs = model.generate(**inputs, max_new_tokens=settings.MAX_NEW_TOKENS)
        return tokenizer.decode(outputs[0], skip_special_tokens=True)
    except Exception as e:
        logger.error(f"Error during summarization: {e}")
        raise


def extract_keywords(text: str) -> list:
    words = text.split()
    freq = {}
    for word in words:
        word = word.lower().strip(".,!?;:")
        if len(word) > 4:
            freq[word] = freq.get(word, 0) + 1
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [word for word, _ in sorted_words[:5]]


def analyze_sentiment(text: str) -> dict:
    """Uses flan-t5 for sentiment — no extra model download needed."""
    try:
        logger.info("Analyzing sentiment")
        prompt = f"Is the sentiment of this text positive, negative, or neutral? Answer with one word only.\n\nText: {text[:500]}"
        inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
        outputs = model.generate(**inputs, max_new_tokens=5)
        label = tokenizer.decode(outputs[0], skip_special_tokens=True).strip().lower()
        # Normalise to a consistent label
        if "positive" in label:
            label = "POSITIVE"
        elif "negative" in label:
            label = "NEGATIVE"
        else:
            label = "NEUTRAL"
        return {"label": label, "score": 1.0}
    except Exception as e:
        logger.error(f"Error during sentiment analysis: {e}")
        raise