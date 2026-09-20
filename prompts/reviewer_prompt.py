import json


def build_reviewer_prompt(cv_data):

    return f"""
You are a senior hiring manager reviewing a CV for a DevOps Engineer position.

Review the following structured CV.

Focus on practical hiring quality:

1. What should be improved
2. What should be removed or reduced
3. What should be rewritten
4. What is missing
5. What changes would make the CV clearer and stronger for a DevOps role

Important:
- Base feedback only on information present in the CV.
- Do not invent achievements, metrics, skills, certifications, or experience.
- If a stronger achievement would require information that is not provided, clearly say that it needs user confirmation.
- Keep recommendations practical and specific.
- Do not recommend changes just for the sake of making the CV longer.

Return ONLY one valid JSON object.

The JSON must contain exactly these fields:

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