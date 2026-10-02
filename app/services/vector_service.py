from sqlalchemy import text
from app.core.database import engine
from app.services.embedding_service import create_embedding


def store_document_chunk(
    document_id: int,
    chunk_text: str,
    page_number=None
):
    embedding = create_embedding(chunk_text)

    query = text("""
        INSERT INTO document_chunks
        (
            document_id,
            chunk_text,
            page_number,
            embedding
        )
        VALUES
        (
            :document_id,
            :chunk_text,
            :page_number,
            CAST(:embedding AS vector)
        )
        RETURNING id;
    """)

    with engine.begin() as connection:
        result = connection.execute(
            query,
            {
                "document_id": document_id,
                "chunk_text": chunk_text,
                "page_number": page_number,
                "embedding": str(embedding)
            }
        )

        return result.fetchone()[0]