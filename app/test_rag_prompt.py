from app.services.llm_service import ask_llm
from app.prompts.rag import RAG_PROMPT


context = """
Company Leave Policy

Employees receive 30 days of annual leave every year.
Annual leave must be approved by the employee's manager.
"""


questions = [
    "How many days of annual leave do employees receive?",
    "Who must approve annual leave?",
    "What is the company's sick leave policy?"
]


for question in questions:

    prompt = RAG_PROMPT.format(
        context=context,
        question=question
    )

    answer = ask_llm(prompt)

    print("\nQUESTION:")
    print(question)

    print("\nANSWER:")
    print(answer)

    print("-" * 60)