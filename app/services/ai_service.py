import logging

logger = logging.getLogger(__name__)

def summarize_text(text: str) -> str:
    logger.info("Summarizing text (lightweight mode)")
    return text[:300]

def extract_keywords(text: str) -> list:
    words = text.split()
    freq = {}
    for word in words:
        word = word.lower().strip(".,!?()[]{}:\"'")
        if len(word) > 4:
            freq[word] = freq.get(word, 0) + 1

    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [word for word, _ in sorted_words[:5]]

def analyze_sentiment(text: str) -> dict:
    logger.info("Sentiment analysis (lightweight mode)")
    return {"label": "UNKNOWN", "score": 0.0}