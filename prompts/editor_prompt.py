import json


def build_editor_prompt(cv_data, suggestions):

    return f"""
You are a professional CV editor specializing in DevOps resumes.

You have the original structured CV and a list of approved suggestions.

Apply ONLY the approved suggestions to improve the CV.

Rules:
- Keep all factual information unchanged.
- Never invent companies, certifications, experience, skills, achievements, metrics, or technologies.
- Do not turn hypothetical suggestions into factual claims.
- Improve wording only when supported by the original CV or approved suggestion.
- Keep the CV concise and professional.
- Preserve important information from the original CV.
- Return exactly one JSON object matching the CV structure.

The JSON must contain exactly these fields:

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

ORIGINAL CV:

{json.dumps(cv_data.model_dump(), indent=2)}

APPROVED SUGGESTIONS:

{json.dumps(suggestions, indent=2)}

Return ONLY valid JSON.
Do not use markdown.
Do not add any explanation before or after the JSON.
"""