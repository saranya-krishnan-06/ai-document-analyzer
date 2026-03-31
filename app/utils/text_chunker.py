def split_text(text: str, chunk_size: int = 150, overlap: int = 30):
    words = text.split()
    chunks = []

    if not words:
        return chunks

    step = chunk_size - overlap
    if step <= 0:
        step = chunk_size

    for i in range(0, len(words), step):
        chunk = " ".join(words[i:i + chunk_size])
        if chunk.strip():
            chunks.append(chunk)

    return chunks