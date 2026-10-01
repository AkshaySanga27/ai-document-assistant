from app.services.llm_service import ask_llm
from app.prompts.extraction import EXTRACTION_PROMPT


text = """
John Smith works as a Software Engineer at ABC Technologies.
His email is john@abc.com and his phone number is
+971501234567.
"""


prompt = EXTRACTION_PROMPT.format(text=text)

result = ask_llm(prompt)

print("\nEXTRACTED INFORMATION:\n")
print(result)