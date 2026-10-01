from app.services.llm_service import ask_llm


prompt = """
Explain Large Language models (LLM)
to a beginner in simple terms.
"""

answer = ask_llm(prompt)

print("\nLLM RESPONSE:\n")
print(answer)