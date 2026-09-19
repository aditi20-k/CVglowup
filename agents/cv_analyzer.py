import json

from google import genai
from app.config import GEMINI_API_KEY
from models.cv_schema import CVData

client = genai.Client(api_key=GEMINI_API_KEY)


def analyze_cv(cv_text):
    prompt = f"""
You are an expert CV analyzer and senior hiring manager.

Analyze the following CV and return ONLY valid JSON.

The JSON must contain:
{{
    "name": "",
    "summary": "",
    "education": [
        {{
            "institution": "",
            "degree": "",
            "period": ""
        }}
    ],
    "experience": [
        {{
            "role": "",
            "company": "",
            "duration": "",
            "responsibilities": []
        }}
    ],
    "skills": [],
    "projects": [
        {{
            "title": "",
            "description": "",
            "technologies": []
        }}
    ],
    "certifications": [],
    "strengths": [],
    "weaknesses": [],
    "suggestions": []
}}

CV:
{cv_text}
"""

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    data = json.loads(response.text)

    return CVData(**data)