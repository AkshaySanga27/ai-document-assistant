from app.services.rag_service import answer_question


question = "What is Retrieval-Augmented Generation?"

result = answer_question(question)


print("\nQUESTION:")
print(question)

print("\nANSWER:")
print(result["answer"])

print("\nSOURCES:")

for source in result["sources"]:

    print(
        f"File: {source['filename']} | "
        f"Page: {source['page_number']} | "
        f"Similarity: {source['similarity']:.4f}"
    )