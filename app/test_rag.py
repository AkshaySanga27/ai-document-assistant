from app.services.retrieval_service import retrieve_documents
from app.services.llm_service import ask_llm
from app.prompts.rag import RAG_PROMPT


documents = [
    "Employees receive 30 days of annual leave every year.",
    "Employees must submit leave requests to their manager.",
    "The company headquarters is located in Dubai.",
    "Employees can work remotely two days per week.",
    "The company provides health insurance to employees."
]


question = "How many vacation days do employees get?"


retrieved_documents = retrieve_documents(
    question,
    documents,
    top_k=3
)


context = "\n".join(
    document
    for document, score in retrieved_documents
)


prompt = RAG_PROMPT.format(
    context=context,
    question=question
)


answer = ask_llm(prompt)


print("\nQUESTION:")
print(question)

print("\nRETRIEVED DOCUMENTS:")

for document, score in retrieved_documents:
    print(f"\nScore: {score:.4f}")
    print(document)


print("\nFINAL ANSWER:")
print(answer)