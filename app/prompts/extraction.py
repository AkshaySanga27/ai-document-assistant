EXTRACTION_PROMPT = """
Extract the following information from the text.

Return ONLY valid JSON.

The JSON must have exactly these keys:

{{
    "name": "",
    "company": "",
    "email": "",
    "phone": ""
}}

If information is missing, use "Not available".

Text:
{text}
"""