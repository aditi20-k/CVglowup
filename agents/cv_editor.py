import json

from google import genai
from app.config import GEMINI_API_KEY
from models.cv_schema import CVData

client = genai.Client(api_key=GEMINI_API_KEY)


def apply_suggestions(cv_data: CVData, suggestions):
    prompt = f"""
You are a professional CV editor.

You have the original structured CV and a list of approved suggestions.

Apply the suggestions to improve the CV for a DevOps Engineer position.

Rules:
- Keep factual information unchanged.
- Do not invent companies, certifications, experience, skills, or achievements.
- Improve wording where suggested.
- Keep the CV professional and concise.
- Return ONLY valid JSON matching the CV structure exactly.

CV:
{json.dumps(cv_data.model_dump(), indent=2)}

APPROVED SUGGESTIONS:
{json.dumps(suggestions, indent=2)}

Return this exact structure:

{{
    "name": "",
    "summary": "",
    "education": [],
    "experience": [],
    "skills": [],
    "projects": [],
    "certifications": [],
    "strengths": [],
    "weaknesses": [],
    "suggestions": []
}}
"""

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    data = json.loads(response.text)

    return CVData(**data)