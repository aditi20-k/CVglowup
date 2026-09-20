# ✦ CVGlowUp

### A CV review and improvement platform built with Python, Gemini, and Streamlit.

CVGlowUp helps candidates turn an existing CV into a more structured and professional version through a guided review workflow.

Instead of directly rewriting the CV, the application first analyzes the content, reviews it from a hiring-manager perspective, allows the user to select the changes they want, and then generates a refined PDF.

---

## ✨ What CVGlowUp Does

**Upload → Analyze → Review → Select → Improve → Generate**

* 📄 Supports **PDF and DOCX** CVs
* 🔍 Extracts and structures CV content
* 👔 Reviews the CV from a **Hiring Manager perspective**
* 💡 Identifies areas that need improvement
* ✅ Lets users choose which suggestions to apply
* ✍️ Improves selected sections while keeping the original facts intact
* 👀 Shows the refined CV before generating the final document
* 📑 Generates a downloadable PDF

---

## 🔄 How It Works

```text
                Upload CV
              PDF / DOCX
                   │
                   ▼
            Extract CV Content
                   │
                   ▼
          Structure CV Information
                   │
                   ▼
             CV Analysis
                   │
                   ▼
        Hiring Manager Review
                   │
                   ▼
          Select Improvements
                   │
                   ▼
          Apply Selected Changes
                   │
                   ▼
           Refined CV Preview
                   │
                   ▼
             Generate PDF
```

The workflow gives the user control over the changes instead of automatically replacing the entire CV.

---

## 🛠️ Tech Stack

| Area            | Technologies       |
| --------------- | ------------------ |
| Language        | Python             |
| Frontend        | Streamlit          |
| CV Parsing      | PyPDF, python-docx |
| Data Validation | Pydantic           |
| Review Engine   | Google Gemini API  |
| Templating      | Jinja2             |
| PDF Generation  | WeasyPrint         |
| Version Control | Git, GitHub        |

---

## 📁 Project Structure

```text
cv-agent/
│
├── agents/
│   ├── cv_analyzer.py
│   ├── cv_editor.py
│   ├── cv_reviewer.py
│   └── __init__.py
│
├── app/
│   ├── config.py
│   ├── pdf_generator.py
│   └── streamlit_app.py
│
├── models/
│   ├── cv_schema.py
│   └── __init__.py
│
├── parsers/
│   ├── pdf_parser.py
│   ├── docx_parser.py
│   └── __init__.py
│
├── prompts/
│   ├── analyzer_prompt.py
│   ├── editor_prompt.py
│   └── reviewer_prompt.py
│
├── templates/
│   └── cv_template.html
│
├── generated/
├── uploads/
│
├── .env
├── .gitignore
├── requirements.txt
└── run.py
```

### Key Components

**`parsers/`**
Handles extraction of text from PDF and DOCX files.

**`models/`**
Defines the structured CV data model using Pydantic.

**`agents/`**
Contains the analysis, review, and editing logic.

**`prompts/`**
Contains the instructions used for different CV processing stages.

**`templates/`**
Contains the HTML/CSS template used to create the final CV.

**`app/`**
Contains the Streamlit interface and PDF generation logic.

---

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd cv-agent
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
pip install google-genai
```

### 5. Add your Gemini API key

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

### 6. Run the application

```bash
python -m streamlit run app/streamlit_app.py
```

---

## 🔐 Security

API credentials are stored in environment variables and are not included in the repository.

The `.gitignore` file excludes:

```text
.env
.venv/
uploads/
generated/
__pycache__/
```

---

## ☁️ DevOps Direction

CVGlowUp is also being developed as a practical **Cloud & DevOps project**.

The application is being prepared for deployment using:

* Docker
* AWS EC2
* Kubernetes
* Jenkins CI/CD

The goal is to take the application from a local Python project to a containerized and automated cloud deployment.

```text
GitHub
   ↓
Jenkins
   ↓
Docker
   ↓
AWS EC2
   ↓
Kubernetes
```

---

## 🎯 Project Focus

This project combines **application development with Cloud and DevOps practices**.

It demonstrates experience with:

* Python application development
* API integration
* Document processing
* Structured data validation
* Git & GitHub
* Containerization
* Cloud deployment
* CI/CD
* Kubernetes

---

## 👩‍💻 Author

### Aditi Kapoor

**B.E. Computer Science & Engineering · Class of 2026**

Cloud & DevOps learner focused on **AWS, Linux, Docker, Kubernetes, CI/CD, and Infrastructure Automation**.
