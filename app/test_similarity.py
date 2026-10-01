from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer("all-MiniLM-L6-v2")


sentences = [
    "Employees receive 30 days of annual leave.",
    "Workers get thirty days of vacation every year.",
    "The company headquarters is located in Dubai."
]


embeddings = model.encode(sentences)


similarity_1 = cosine_similarity(
    [embeddings[0]],
    [embeddings[1]]
)[0][0]


similarity_2 = cosine_similarity(
    [embeddings[0]],
    [embeddings[2]]
)[0][0]


print("Sentence 1:")
print(sentences[0])

print("\nSentence 2:")
print(sentences[1])

print("\nSimilarity:")
print(similarity_1)


print("\n-----------------------------")


print("\nSentence 1:")
print(sentences[0])

print("\nSentence 3:")
print(sentences[2])

print("\nSimilarity:")
print(similarity_2)