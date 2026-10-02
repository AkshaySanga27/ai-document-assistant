from app.services.vector_search_service import search_similar_chunks
from app.services.llm_service import ask_llm
from app.prompts.rag import RAG_PROMPT


question = "What is Retrieval-Augmented Generation?"

# 1. Retrieve relevant chunks
results = search_similar_chunks(question, top_k=3)

# 2. Build context
context = "\n\n".join(
    result.chunk_text
    for result in results
)

# 3. Build RAG prompt
prompt = RAG_PROMPT.format(
    context=context,
    question=question
)

# 4. Ask the LLM
answer = ask_llm(prompt)

print("\nQUESTION:")
print(question)

print("\nRETRIEVED CONTEXT:")
print(context)

print("\nLLM ANSWER:")
print(answer)