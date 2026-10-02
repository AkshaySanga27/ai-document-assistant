from app.services.vector_search_service import search_similar_chunks
from app.services.llm_service import ask_llm
from app.prompts.rag import RAG_PROMPT


def answer_question(question: str, top_k: int = 3):

    # 1. Retrieve relevant chunks
    results = search_similar_chunks(
        question,
        top_k=top_k
    )

    # 2. Handle no results
    if not results:
        return {
            "answer": "I don't know based on the provided document.",
            "sources": []
        }

    # 3. Build context
    context_parts = []

    sources = []

    for result in results:

        context_parts.append(
            f"Source: {result.filename}, "
            f"Page: {result.page_number}\n"
            f"{result.chunk_text}"
        )

        sources.append({
            "filename": result.filename,
            "page_number": result.page_number,
            "similarity": float(result.similarity)
        })

    context = "\n\n".join(context_parts)

    # 4. Build RAG prompt
    prompt = RAG_PROMPT.format(
        context=context,
        question=question
    )

    # 5. Ask Llama
    answer = ask_llm(prompt)

    return {
        "answer": answer,
        "sources": sources
    }