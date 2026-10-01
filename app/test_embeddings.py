from app.services.embedding_service import create_embedding


text = "Employees receive 30 days of annual leave."


embedding = create_embedding(text)


print("Embedding created successfully.")
print("Number of dimensions:", len(embedding))
print("First 10 values:")
print(embedding[:10])