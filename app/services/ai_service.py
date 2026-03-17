from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from app.core.config import settings
from app.core.logger import logger
import logging
logger = logging.getLogger(__name__)

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")


sentiment_analyzer = pipeline(
    "sentiment-analysis"
)

def summarize_text(text: str) -> str:
    try:
        logger.info("Summarizing text")

        prompt = f"Summarize the following text:\n\n{text}"

        inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

        outputs = model.generate(
            **inputs,
            max_new_tokens=60
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
        if len(word) > 4:
            freq[word] = freq.get(word, 0) + 1

    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [word for word, count in sorted_words[:5]]


def analyze_sentiment(text: str) -> dict:
    result = sentiment_analyzer(text)
    logger.info("Analyzing sentiment")
    return result[0]