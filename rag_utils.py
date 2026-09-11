from io import BytesIO

from docx import Document
from pypdf import PdfReader

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text(uploaded_file):
    filename = uploaded_file.name.lower()
    file_bytes = BytesIO(uploaded_file.getvalue())

    if filename.endswith(".pdf"):
        reader = PdfReader(file_bytes)
        return "\n".join(page.extract_text() or "" for page in reader.pages)

    if filename.endswith(".docx"):
        document = Document(file_bytes)
        return "\n".join(
            paragraph.text for paragraph in document.paragraphs
        )

    if filename.endswith(".txt"):
        return uploaded_file.getvalue().decode(
            "utf-8",
            errors="replace"
        )

    raise ValueError("Unsupported file type.")

def split_text(text, chunk_size=800, overlap=150):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks

def retrieve_chunks(question, chunks, top_k=3):
    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2)
    )
    chunk_vectors = vectorizer.fit_transform(chunks)
    question_vector = vectorizer.transform([question])

    scores = cosine_similarity(
        question_vector,
        chunk_vectors
    ).flatten()

    top_indices = scores.argsort()[-top_k:][::-1]

    results = []

    for index in top_indices:
        results.append(
            {
                "text": chunks[index],
                "score": float(scores[index])
            }
        )

    return results