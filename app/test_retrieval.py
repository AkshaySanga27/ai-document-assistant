from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer("all-MiniLM-L6-v2")


documents = [
    "Employees receive 30 days of annual leave every year.",
    "Employees must submit leave requests to their manager.",
    "The company headquarters is located in Dubai.",
    "Employees can work remotely two days per week.",
    "The company provides health insurance to employees."
]


question = "How many vacation days do employees get?"


document_embeddings = model.encode(documents)

question_embedding = model.encode([question])


similarities = cosine_similarity(
    question_embedding,
    document_embeddings
)[0]


results = list(zip(documents, similarities))


results.sort(
    key=lambda x: x[1],
    reverse=True
)


print("\nQUESTION:")
print(question)

print("\nMOST RELEVANT DOCUMENTS:\n")


for document, score in results:

    print(f"Score: {score:.4f}")
    print(document)
    print("-" * 60)