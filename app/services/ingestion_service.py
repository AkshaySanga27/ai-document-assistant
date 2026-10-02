from sqlalchemy import text

from app.core.database import engine
from app.services.pdf_service import extract_text_from_pdf
from app.services.chunking_service import chunk_text
from app.services.embedding_service import create_embedding


def ingest_pdf(file_path: str, filename: str):

    # 1. Extract text from PDF
    pages = extract_text_from_pdf(file_path)

    # 2. Create document record
    with engine.begin() as connection:

        result = connection.execute(
            text("""
                INSERT INTO documents (filename)
                VALUES (:filename)
                RETURNING id;
            """),
            {
                "filename": filename
            }
        )

        document_id = result.fetchone()[0]

    total_chunks = 0

    # 3. Process every page
    for page in pages:

        page_number = page["page_number"]
        page_text = page["text"]

        # 4. Split page text into chunks
        chunks = chunk_text(
            page_text,
            chunk_size=500,
            overlap=50
        )

        # 5. Process every chunk
        for chunk in chunks:

            # 6. Generate embedding
            embedding = create_embedding(chunk)

            # 7. Store chunk + embedding
            with engine.begin() as connection:

                connection.execute(
                    text("""
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
                        );
                    """),
                    {
                        "document_id": document_id,
                        "chunk_text": chunk,
                        "page_number": page_number,
                        "embedding": str(embedding)
                    }
                )

            total_chunks += 1

    return {
        "document_id": document_id,
        "filename": filename,
        "pages": len(pages),
        "chunks": total_chunks
    }