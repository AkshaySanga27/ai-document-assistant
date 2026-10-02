from app.services.vector_search_service import search_similar_chunks


question = "What is Retrieval-Augmented Generation?"

results = search_similar_chunks(question, top_k=3)

print("\nVECTOR SEARCH RESULTS\n")

for result in results:
    print("Chunk ID:", result.id)
    print("Document ID:", result.document_id)
    print("Similarity:", result.similarity)
    print("Text:", result.chunk_text)
    print("-" * 60)