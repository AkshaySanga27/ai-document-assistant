from app.services.llm_service import ask_llm
from app.prompts.classification import CLASSIFICATION_PROMPT


messages = [
    "My payment was deducted twice.",
    "What documents do I need to open an account?",
    "Please send me my account statement.",
    "The new dashboard is very easy to use."
]


for message in messages:

    prompt = CLASSIFICATION_PROMPT.format(
        message=message
    )

    result = ask_llm(prompt)

    print("\nMessage:")
    print(message)

    print("Classification:")
    print(result)