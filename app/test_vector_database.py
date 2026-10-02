from sqlalchemy import text

from app.core.database import engine
from app.services.vector_service import store_document_chunk


# Create a test document
with engine.begin() as connection:

    result = connection.execute(
        text("""
            INSERT INTO documents (filename)
            VALUES (:filename)
            RETURNING id;
        """),
        {
            "filename": "test_document.pdf"
        }
    )

    document_id = result.fetchone()[0]


# Create and store embedding
chunk_id = store_document_chunk(
    document_id=document_id,
    chunk_text="Retrieval-Augmented Generation allows an AI system to retrieve relevant information from documents before generating an answer.",
    page_number=1
)

print("\nVECTOR DATABASE TEST SUCCESSFUL")
print("Document ID:", document_id)
print("Chunk ID:", chunk_id)