import json

from google import genai
from app.config import GEMINI_API_KEY
from models.cv_schema import CVData

client = genai.Client(api_key=GEMINI_API_KEY)


def review_cv(cv_data: CVData):
    prompt = f"""
You are a senior hiring manager reviewing a CV for a DevOps Engineer position.

Review the following structured CV.

Identify:
1. What should be improved
2. What should be removed or reduced
3. What should be rewritten
4. What is missing
5. What changes would make the CV stronger for a DevOps role

Return ONLY valid JSON in this exact structure:

{{
    "overall_review": "",
    "priority_changes": [],
    "section_reviews": [],
    "missing_elements": [],
    "rewrite_suggestions": []
}}

CV DATA:
{json.dumps(cv_data.model_dump(), indent=2)}
"""

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    return json.loads(response.text)