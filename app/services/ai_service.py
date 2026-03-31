from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import logging

logger = logging.getLogger(__name__)

tokenizer = None
model = None
sentiment_analyzer = None


def load_models():
    global tokenizer, model, sentiment_analyzer

    if tokenizer is None or model is None:
        tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
        model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")

    if sentiment_analyzer is None:
        sentiment_analyzer = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )

    return tokenizer, model, sentiment_analyzer


def summarize_text(text: str) -> str:
    try:
        logger.info("Summarizing text")

        tokenizer, model, _ = load_models()

        prompt = f"""
Summarize the following document in 2 to 3 concise sentences.

Document:
{text}

Summary:
"""

        inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

        outputs = model.generate(
            **inputs,
            max_new_tokens=80
        )

        summary = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
        return summary

    except Exception as e:
        logger.error(f"Error during summarization: {str(e)}")
        raise


def extract_keywords(text: str) -> list:
    words = text.split()
    freq = {}

    for word in words:
        word = word.lower().strip(".,!?()[]{}:\"'")
        if len(word) > 4:
            freq[word] = freq.get(word, 0) + 1

    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [word for word, count in sorted_words[:5]]


def analyze_sentiment(text: str) -> dict:
    _, _, sentiment_analyzer = load_models()
    result = sentiment_analyzer(text)
    logger.info("Analyzing sentiment")
    return result[0]