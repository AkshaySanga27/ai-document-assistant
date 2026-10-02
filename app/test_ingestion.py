from app.services.ingestion_service import ingest_pdf


pdf_path = "documents/sample_rag_test.pdf"

result = ingest_pdf(
    file_path=pdf_path,
    filename="sample_rag_test.pdf"
)

print("\nPDF INGESTION SUCCESSFUL\n")

print("Document ID:", result["document_id"])
print("Filename:", result["filename"])
print("Pages:", result["pages"])
print("Chunks:", result["chunks"])