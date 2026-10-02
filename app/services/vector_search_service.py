from sqlalchemy import text

from app.core.database import engine
from app.services.embedding_service import create_embedding


def search_similar_chunks(question: str, top_k: int = 3):

    question_embedding = create_embedding(question)

    query = text("""
        SELECT
            dc.id,
            dc.document_id,
            d.filename,
            dc.chunk_text,
            dc.page_number,
            1 - (
                dc.embedding <=> CAST(:embedding AS vector)
            ) AS similarity
        FROM document_chunks dc
        JOIN documents d
            ON dc.document_id = d.id
        WHERE dc.embedding IS NOT NULL
        ORDER BY dc.embedding <=> CAST(:embedding AS vector)
        LIMIT :top_k
    """)

    with engine.connect() as connection:

        result = connection.execute(
            query,
            {
                "embedding": str(question_embedding),
                "top_k": top_k
            }
        )

        return result.fetchall()