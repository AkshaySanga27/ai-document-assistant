from sentence_transformers import SentenceTransformer


MODEL_NAME = "all-MiniLM-L6-v2"    #For all-MiniLM-L6-v2, the embedding dimension is 384.

model = SentenceTransformer(MODEL_NAME)


def create_embedding(text: str):  
    embedding = model.encode(text) #Encode converts text into a vector.

    return embedding.tolist()