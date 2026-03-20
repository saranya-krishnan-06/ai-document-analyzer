#app/services/ai_service.py
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from app.core.config import settings
from app.core.logger import logger
import logging
logger = logging.getLogger(__name__)

tokenizer = None
model = None

def get_model():
    global tokenizer, model

    if tokenizer is None or model is None:
        tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
        model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")

    return tokenizer, model


sentiment_analyzer = pipeline(
   "sentiment-analysis"
)

def summarize_text(text: str) -> str:
    #return text [:300]
    try:
        logger.info("Summarizing text")
        tokenizer, model = get_model()

        prompt = f"Summarize the following text:\n\n{text}"

        inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

        outputs = model.generate(
            **inputs,
            max_new_tokens=60,
            temperature=0.3
        )

        summary = tokenizer.decode(outputs[0], skip_special_tokens=True)


        return summary

    except Exception as e:
        logger.error(f"Error during summarization: {str(e)}")
        raise



def extract_keywords(text: str) -> list:
    # Simple keyword extraction using most frequent words
    words = text.split()
    freq = {}
    for word in words:
        word = word.lower()
        #word = word.lower().strip(".,!?()[]{}:\"'")
        if len(word) > 4:
            freq[word] = freq.get(word, 0) + 1

    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [word for word, count in sorted_words[:5]]


def analyze_sentiment(text: str) -> dict:
    #return {"label": "UNKNOWN", "score": 0.0}
    result = sentiment_analyzer(text)
    logger.info("Analyzing sentiment")
    return result[0]