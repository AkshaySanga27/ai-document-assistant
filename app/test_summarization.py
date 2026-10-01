from app.services.llm_service import ask_llm
from app.prompts.summarization import SUMMARY_PROMPT


text = """
Artificial intelligence is increasingly being used in businesses
to automate repetitive tasks, analyze large amounts of data, improve
customer service, and support decision making. Generative AI has
expanded these capabilities by allowing applications to generate
text, code, summaries, and other forms of content.
"""


prompt = SUMMARY_PROMPT.format(text=text)

answer = ask_llm(prompt)

print("\nSUMMARY:\n")
print(answer)