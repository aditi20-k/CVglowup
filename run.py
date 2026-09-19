from parsers.pdf_parser import extract_text_from_pdf
from agents.cv_analyzer import analyze_cv
from agents.cv_reviewer import review_cv
from agents.cv_editor import apply_suggestions
from app.pdf_generator import generate_cv_pdf


pdf_path = "uploads/sample_cv.pdf"

cv_text = extract_text_from_pdf(pdf_path)

print("CV TEXT EXTRACTED ✅")

result = analyze_cv(cv_text)

print("\nAI ANALYSIS 🤖")
print("--------------------")
print(result.model_dump_json(indent=2))

review = review_cv(result)

print("\nSENIOR MANAGER REVIEW 👔")
print("--------------------")
print(review)

approved_suggestions = review.get("rewrite_suggestions", [])

updated_cv = apply_suggestions(result, approved_suggestions)

print("\nUPDATED CV ✨")
print("--------------------")
print(updated_cv.model_dump_json(indent=2))

pdf_path = generate_cv_pdf(updated_cv)

print("\nPDF GENERATED 📄")
print("--------------------")
print(f"Improved CV saved at: {pdf_path}")