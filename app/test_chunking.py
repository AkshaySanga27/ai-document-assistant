from app.services.pdf_service import extract_text_from_pdf
from app.services.chunking_service import chunk_text


pdf_path = "documents/sample_rag_test.pdf"

pages = extract_text_from_pdf(pdf_path)

print("\nPDF CHUNKING TEST\n")

for page in pages:

    chunks = chunk_text(
        page["text"],
        chunk_size=50,
        overlap=10
    )

    print(f"PAGE: {page['page_number']}")
    print(f"NUMBER OF CHUNKS: {len(chunks)}")

    for index, chunk in enumerate(chunks, start=1):

        print(f"\nCHUNK {index}:")
        print(chunk)

    print("\n" + "=" * 70)