from transformers import pipeline

# Load models once when app starts
summarizer = pipeline(
    "text-generation",
    model="google/flan-t5-small"
)

sentiment_analyzer = pipeline(
    "sentiment-analysis"
)

def summarize_text(text: str) -> str:
    prompt = f"Summarize the following text:\n\n{text}"
    result = summarizer(
        prompt,
        max_new_tokens=150,
        do_sample=False
    )
    return result[0]["generated_text"]


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
    return result[0]