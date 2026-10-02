from app.services.pdf_service import extract_text_from_pdf


pdf_path = "documents/sample_rag_test.pdf"

pages = extract_text_from_pdf(pdf_path)

print("\nPDF EXTRACTION TEST\n")

for page in pages:
    print("PAGE:", page["page_number"])
    print(page["text"][:500])
    print("-" * 60)