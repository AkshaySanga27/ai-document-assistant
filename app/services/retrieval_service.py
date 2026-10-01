from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)


def retrieve_documents(
    question: str,
    documents: list[str],
    top_k: int = 3
):
    document_embeddings = model.encode(documents)

    question_embedding = model.encode([question])

    similarities = cosine_similarity(
        question_embedding,
        document_embeddings
    )[0]

    results = list(
        zip(documents, similarities)
    )

    results.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return results[:top_k]