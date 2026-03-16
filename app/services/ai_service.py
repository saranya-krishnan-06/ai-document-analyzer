from transformers import pipeline
from app.core.config import settings
from app.core.logger import logger
import logging
logger = logging.getLogger(__name__)

# Load models once when app starts
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

sentiment_analyzer = pipeline(
    "sentiment-analysis"
)

def summarize_text(text: str):
    result = summarizer(text, max_length=120, min_length=30, do_sample=False)
    return result[0]["summary_text"]


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