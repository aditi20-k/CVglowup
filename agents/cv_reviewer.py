import json

from google import genai

from app.config import GEMINI_API_KEY
from models.cv_schema import CVData
from prompts.reviewer_prompt import build_reviewer_prompt


client = genai.Client(api_key=GEMINI_API_KEY)


def extract_json(text):
    text = text.strip()

    try:
        return json.loads(text)

    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")

        if start == -1 or end == -1:
            raise ValueError(
                "Could not find a valid JSON object in Gemini response."
            )

        json_text = text[start:end + 1]

        try:
            return json.loads(json_text)

        except json.JSONDecodeError as e:
            raise ValueError(
                f"Gemini returned invalid JSON: {e}"
            )


def review_cv(cv_data: CVData):

    prompt = build_reviewer_prompt(cv_data)

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt,
        config={
            "response_mime_type": "application/json"
        }
    )

    if not response.text:
        raise ValueError(
            "Gemini returned an empty response."
        )

    data = extract_json(response.text)

    return data