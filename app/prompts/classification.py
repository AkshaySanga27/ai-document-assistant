CLASSIFICATION_PROMPT = """
Classify the following customer message into exactly one category:

- complaint
- question
- request
- feedback

Return only the category.

Customer message:
{message}
"""