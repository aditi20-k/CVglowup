def build_analyzer_prompt(cv_text):

    return f"""
You are an expert CV analyzer and senior hiring manager.

Analyze the following CV.

Return ONLY one valid JSON object.

Do not use markdown.
Do not use ```json.
Do not add any explanation before or after the JSON.

The JSON must contain exactly these fields:

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

Important:
- Use only information actually present in the CV.
- Do not invent experience, achievements, metrics, certifications, companies, or skills.
- If information is missing, use an empty string or empty list.
- Return exactly one JSON object.

CV:
{cv_text}
"""