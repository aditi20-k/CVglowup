import os
import tempfile

import streamlit as st
import streamlit.components.v1 as components

from pathlib import Path

from parsers.pdf_parser import extract_text_from_pdf
from parsers.docx_parser import extract_text_from_docx

from agents.cv_analyzer import analyze_cv
from agents.cv_reviewer import review_cv
from agents.cv_editor import apply_suggestions

from app.pdf_generator import generate_cv_pdf

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="CVGlowUp",
    page_icon="✦",
    layout="wide"
)


# ==========================================
# GLOBAL UI
# ==========================================

st.markdown(
    """
    <style>

    /* ---------- APP ---------- */

    .stApp {
        background:
            radial-gradient(
                circle at 5% 0%,
                rgba(108, 92, 231, 0.06),
                transparent 25%
            ),
            #fafaff;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 2rem;
        padding-bottom: 5rem;
    }


    /* ---------- TYPOGRAPHY ---------- */

    h1, h2, h3 {
        color: #181927 !important;
        letter-spacing: -0.6px;
    }

    p {
        color: #626575;
    }


    /* ---------- BUTTONS ---------- */

    div.stButton > button {
        min-height: 46px;
        border-radius: 12px;
        border: 1px solid #dedcff;
        padding: 0.55rem 1.25rem;
        font-weight: 650;
        font-size: 14px;

        color: #111111 !important;

        transition: all 0.2s ease;

        box-shadow:
            0 5px 18px rgba(67, 57, 150, 0.06);
    }


    /* Force normal button text to stay visible */

    div.stButton > button p,
    div.stButton > button span {
        color: #111111 !important;
        font-weight: 650 !important;
    }


    div.stButton > button:hover {
        transform: translateY(-2px);
        border-color: #8479ff;

        box-shadow:
            0 10px 28px rgba(67, 57, 150, 0.12);
    }


    /* ---------- PRIMARY BUTTONS ---------- */

    div.stButton > button[kind="primary"] {
        color: #ffffff !important;
        border: none;

        background:
            linear-gradient(
                135deg,
                #6558f5,
                #8175ff
            ) !important;

        box-shadow:
            0 10px 25px rgba(101, 88, 245, 0.22);
    }


    div.stButton > button[kind="primary"] p,
    div.stButton > button[kind="primary"] span {
        color: #ffffff !important;
        font-weight: 650 !important;
    }


    div.stButton > button[kind="primary"]:hover {
        box-shadow:
            0 14px 32px rgba(101, 88, 245, 0.30);
    }


    /* ---------- DOWNLOAD BUTTON ---------- */

    div.stDownloadButton > button {
        min-height: 46px;
        border-radius: 12px;
        border: 1px solid #dedcff;

        color: #111111 !important;

        font-weight: 650;
        font-size: 14px;

        background: white !important;

        transition: all 0.2s ease;

        box-shadow:
            0 5px 18px rgba(67, 57, 150, 0.06);
    }


    div.stDownloadButton > button p,
    div.stDownloadButton > button span {
        color: #111111 !important;
        font-weight: 650 !important;
    }


    div.stDownloadButton > button:hover {
        transform: translateY(-2px);
        border-color: #8479ff;

        box-shadow:
            0 10px 28px rgba(67, 57, 150, 0.12);
    }


    /* ---------- FILE UPLOADER ---------- */

    [data-testid="stFileUploader"] {
        background: rgba(255,255,255,0.86);
        border: 1.5px dashed #c9c5f4;
        border-radius: 20px;
        padding: 18px;

        box-shadow:
            0 12px 35px rgba(50,45,110,0.05);
    }


    /* ---------- ALERTS ---------- */

    [data-testid="stAlert"] {
        border-radius: 14px;
        border: 1px solid #e5e3f5;
    }


    /* ---------- CHECKBOX ---------- */

    [data-testid="stCheckbox"] {
        margin-top: 8px;
    }


    /* ---------- DIVIDER ---------- */

    hr {
        border-color: #e9e8f1;
        margin-top: 34px;
        margin-bottom: 34px;
    }


    /* ---------- CONTAINERS ---------- */

    [data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 16px !important;
        border-color: #e7e5f1 !important;

        background: rgba(255,255,255,0.72);

        box-shadow:
            0 8px 25px rgba(45,40,100,0.035);
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==========================================
# HERO
# ==========================================

hero_html = """
<!DOCTYPE html>
<html>
<head>

<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family:
        Inter,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;
    background: transparent;
}

.hero {
    height: 575px;
    position: relative;
    overflow: hidden;
    border-radius: 30px;

    background:
        radial-gradient(
            circle at 85% 20%,
            rgba(116, 99, 255, 0.17),
            transparent 30%
        ),
        radial-gradient(
            circle at 70% 90%,
            rgba(100, 155, 255, 0.10),
            transparent 28%
        ),
        linear-gradient(
            135deg,
            #ffffff 0%,
            #f8f7ff 52%,
            #eff0ff 100%
        );

    border: 1px solid rgba(110,100,190,0.10);

    box-shadow:
        0 25px 70px rgba(55,50,120,0.10);

    padding: 58px 65px;
}


/* subtle grid */

.hero:before {
    content: "";
    position: absolute;
    inset: 0;

    background-image:
        linear-gradient(
            rgba(100,90,180,0.035) 1px,
            transparent 1px
        ),
        linear-gradient(
            90deg,
            rgba(100,90,180,0.035) 1px,
            transparent 1px
        );

    background-size: 38px 38px;

    mask-image:
        linear-gradient(
            to right,
            transparent,
            black 42%,
            black
        );
}


/* content */

.content {
    position: relative;
    z-index: 5;
    width: 51%;
}


/* brand */

.brand {
    display: flex;
    align-items: center;
    gap: 10px;

    font-size: 20px;
    font-weight: 750;

    color: #202132;

    margin-bottom: 58px;
}

.brand-icon {
    width: 36px;
    height: 36px;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 11px;

    background:
        linear-gradient(
            135deg,
            #7464ff,
            #5b50e8
        );

    color: white;

    box-shadow:
        0 8px 22px rgba(99,91,255,0.25);
}


/* eyebrow */

.eyebrow {
    display: inline-block;

    padding: 7px 12px;

    border-radius: 30px;

    background: #f0eeff;

    color: #6559e9;

    font-size: 11px;
    font-weight: 750;

    letter-spacing: 0.6px;

    margin-bottom: 18px;
}


/* title */

.title {
    margin: 0;

    color: #171827;

    font-size: 56px;

    line-height: 1.04;

    letter-spacing: -2.8px;

    font-weight: 780;
}

.title span {
    background:
        linear-gradient(
            90deg,
            #6559f4,
            #8a72ff,
            #5d8eff
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}


/* description */

.description {
    margin-top: 22px;

    max-width: 500px;

    color: #686b7a;

    font-size: 16px;

    line-height: 1.65;
}


/* mini features */

.features {
    display: flex;
    gap: 22px;

    margin-top: 30px;
}

.feature {
    display: flex;
    align-items: center;
    gap: 7px;

    color: #666979;

    font-size: 12px;
    font-weight: 600;
}

.tick {
    width: 19px;
    height: 19px;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 50%;

    background: #ebe9ff;

    color: #6257ed;

    font-size: 10px;
}


/* visual */

.visual {
    position: absolute;

    right: 28px;
    top: 25px;

    width: 49%;
    height: 530px;

    z-index: 3;
}


/* glow */

.visual-glow {
    position: absolute;

    width: 310px;
    height: 310px;

    right: 80px;
    top: 95px;

    border-radius: 50%;

    background:
        rgba(106,91,255,0.12);

    filter: blur(55px);
}


/* document */

.document {
    position: absolute;

    right: 105px;
    top: 82px;

    width: 265px;
    height: 350px;

    background:
        rgba(255,255,255,0.96);

    border:
        1px solid rgba(90,80,170,0.12);

    border-radius: 17px;

    padding: 27px;

    transform: rotate(5deg);

    box-shadow:
        0 25px 60px rgba(50,45,110,0.17);
}


/* document header */

.doc-header {
    display: flex;
    gap: 11px;

    margin-bottom: 22px;
}

.avatar {
    width: 40px;
    height: 40px;

    border-radius: 11px;

    background:
        linear-gradient(
            135deg,
            #dcd8ff,
            #eeeaff
        );
}

.name-line {
    width: 88px;
    height: 8px;

    background: #292b38;

    border-radius: 10px;

    margin-top: 4px;
}

.role-line {
    width: 66px;
    height: 6px;

    background: #b9bbc5;

    border-radius: 10px;

    margin-top: 8px;
}


/* document sections */

.section {
    margin-top: 20px;
}

.heading {
    width: 58px;
    height: 7px;

    background: #6a5df4;

    border-radius: 10px;

    margin-bottom: 10px;
}

.line {
    height: 5px;

    background: #e1e2e8;

    border-radius: 10px;

    margin: 7px 0;
}

.line.medium {
    width: 82%;
}

.line.short {
    width: 62%;
}


/* feedback card */

.feedback {
    position: absolute;

    right: 18px;
    top: 74px;

    width: 150px;

    padding: 15px;

    border-radius: 15px;

    background:
        rgba(255,255,255,0.90);

    backdrop-filter: blur(16px);

    border:
        1px solid rgba(100,90,180,0.12);

    box-shadow:
        0 15px 38px rgba(45,40,100,0.12);

    z-index: 5;
}

.feedback-icon {
    width: 28px;
    height: 28px;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 9px;

    background: #efedff;

    color: #6659ee;

    margin-bottom: 8px;
}

.feedback-title {
    font-size: 11px;

    font-weight: 750;

    color: #292a38;
}

.feedback-text {
    font-size: 9px;

    color: #888a97;

    margin-top: 4px;
}


/* changes card */

.changes {
    position: absolute;

    left: 20px;
    bottom: 55px;

    width: 165px;

    padding: 15px;

    background:
        rgba(255,255,255,0.91);

    backdrop-filter: blur(15px);

    border:
        1px solid rgba(100,90,180,0.12);

    border-radius: 15px;

    box-shadow:
        0 15px 38px rgba(45,40,100,0.11);

    z-index: 6;
}

.changes-label {
    font-size: 9px;

    color: #858795;

    font-weight: 650;

    letter-spacing: 0.4px;
}

.change-row {
    display: flex;
    align-items: center;

    gap: 8px;

    margin-top: 10px;
}

.change-dot {
    width: 8px;
    height: 8px;

    border-radius: 50%;

    background: #6a5df3;
}

.change-text {
    font-size: 10px;

    color: #555766;
}


/* floating dots */

.dot {
    position: absolute;

    width: 7px;
    height: 7px;

    border-radius: 50%;

    background: #7568f5;

    opacity: 0.35;
}

.dot.one {
    right: 370px;
    top: 75px;
}

.dot.two {
    right: 70px;
    bottom: 100px;

    width: 11px;
    height: 11px;
}

.dot.three {
    right: 410px;
    bottom: 120px;

    width: 5px;
    height: 5px;
}

</style>

</head>

<body>

<div class="hero">

    <div class="content">

        <div class="brand">
            <div class="brand-icon">✦</div>
            CVGlowUp
        </div>

        <div class="eyebrow">
            SMARTER CV. STRONGER FIRST IMPRESSION.
        </div>

        <h1 class="title">
            Your CV,<br>
            <span>but better.</span>
        </h1>

        <div class="description">
            Refine your CV with focused feedback,
            stronger wording and a cleaner professional
            structure — all in one place.
        </div>

        <div class="features">

            <div class="feature">
                <div class="tick">✓</div>
                Recruiter-focused
            </div>

            <div class="feature">
                <div class="tick">✓</div>
                Personalised feedback
            </div>

            <div class="feature">
                <div class="tick">✓</div>
                Ready to download
            </div>

        </div>

    </div>


    <div class="visual">

        <div class="visual-glow"></div>

        <div class="dot one"></div>
        <div class="dot two"></div>
        <div class="dot three"></div>


        <div class="feedback">

            <div class="feedback-icon">
                ✦
            </div>

            <div class="feedback-title">
                Hiring review
            </div>

            <div class="feedback-text">
                Clarity & impact checked
            </div>

        </div>


        <div class="document">

            <div class="doc-header">

                <div class="avatar"></div>

                <div>
                    <div class="name-line"></div>
                    <div class="role-line"></div>
                </div>

            </div>


            <div class="section">

                <div class="heading"></div>

                <div class="line medium"></div>
                <div class="line"></div>
                <div class="line short"></div>

            </div>


            <div class="section">

                <div class="heading"></div>

                <div class="line"></div>
                <div class="line medium"></div>
                <div class="line short"></div>

            </div>


            <div class="section">

                <div class="heading"></div>

                <div class="line medium"></div>
                <div class="line"></div>

            </div>

        </div>


        <div class="changes">

            <div class="changes-label">
                SUGGESTED CHANGES
            </div>

            <div class="change-row">
                <div class="change-dot"></div>
                <div class="change-text">
                    Stronger summary
                </div>
            </div>

            <div class="change-row">
                <div class="change-dot"></div>
                <div class="change-text">
                    Clearer skills
                </div>
            </div>

            <div class="change-row">
                <div class="change-dot"></div>
                <div class="change-text">
                    Better impact
                </div>
            </div>

        </div>

    </div>

</div>

</body>
</html>
"""

components.html(
    hero_html,
    height=600,
    scrolling=False
)


# ==========================================
# UPLOAD SECTION
# ==========================================

st.markdown("## Upload your CV")
st.caption("PDF or DOCX • Maximum file size 200MB")

uploaded_file = st.file_uploader(
    "Choose your CV",
    type=["pdf", "docx"],
    label_visibility="collapsed"
)


# ==========================================
# ANALYZE
# ==========================================

if uploaded_file:

    st.success(
        f"✓ {uploaded_file.name} is ready"
    )

    if st.button(
        "Review my CV →",
        type="primary"
    ):

        with st.spinner(
            "Reviewing your CV..."
        ):

            temp_path = None

            try:

                suffix = os.path.splitext(
                    uploaded_file.name
                )[1].lower()

                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=suffix
                ) as temp_file:

                    temp_file.write(
                        uploaded_file.getbuffer()
                    )

                    temp_path = temp_file.name

                # ------------------------------
                # EXTRACT TEXT
                # ------------------------------

                if suffix == ".pdf":

                    cv_text = extract_text_from_pdf(
                        temp_path
                    )

                elif suffix == ".docx":

                    cv_text = extract_text_from_docx(
                        temp_path
                    )

                else:

                    st.error(
                        "Please upload a PDF or DOCX file."
                    )

                    st.stop()

                # ------------------------------
                # ANALYZE CV
                # ------------------------------

                cv_data = analyze_cv(
                    cv_text
                )

                review = review_cv(
                    cv_data
                )

                # ------------------------------
                # SAVE RESULTS
                # ------------------------------

                st.session_state[
                    "cv_data"
                ] = cv_data

                st.session_state[
                    "review"
                ] = review

                st.session_state.pop(
                    "updated_cv",
                    None
                )

                st.session_state.pop(
                    "generated_pdf",
                    None
                )

                st.success(
                    "Your CV review is ready."
                )

            except Exception as e:

                st.error(
                    f"Something went wrong: {e}"
                )

            finally:

                if temp_path and os.path.exists(
                    temp_path
                ):

                    os.remove(temp_path)

# ==========================================
# REVIEW DASHBOARD
# ==========================================

if "review" in st.session_state:

    review = st.session_state["review"]
    cv_data = st.session_state["cv_data"]


    st.divider()

    st.header(
        "Hiring Manager Feedback"
    )

    st.caption(
        "Review the suggestions below and choose the changes you want to keep."
    )


    # --------------------------------------
    # OVERALL REVIEW
    # --------------------------------------

    with st.container(border=True):

        st.markdown(
            "**Overall impression**"
        )

        st.write(
            review.get(
                "overall_review",
                ""
            )
        )


    # --------------------------------------
    # PRIORITY CHANGES
    # --------------------------------------

    st.subheader(
        "What needs attention"
    )

    priority_changes = review.get(
        "priority_changes",
        []
    )

    selected_priority = []


    for i, item in enumerate(
        priority_changes
    ):

        with st.container(border=True):

            st.markdown(
                f"**CHANGE {i + 1}**"
            )

            st.write(item)

            selected = st.checkbox(
                "Keep this change",
                value=True,
                key=f"priority_{i}"
            )

            if selected:

                selected_priority.append(
                    item
                )


    # --------------------------------------
    # REWRITE SUGGESTIONS
    # --------------------------------------

    st.subheader(
        "Suggested improvements"
    )

    rewrite_suggestions = review.get(
        "rewrite_suggestions",
        []
    )

    selected_rewrites = []


    for i, item in enumerate(
        rewrite_suggestions
    ):

        with st.container(border=True):

            st.markdown(
                f"**SUGGESTION {i + 1}**"
            )

            st.write(item)

            selected = st.checkbox(
                "Keep this suggestion",
                value=True,
                key=f"rewrite_{i}"
            )

            if selected:

                selected_rewrites.append(
                    item
                )


    # --------------------------------------
    # SELECTED COUNT
    # --------------------------------------

    selected_count = (
        len(selected_priority)
        + len(selected_rewrites)
    )

    st.info(
        f"✦ {selected_count} changes selected"
    )


    # --------------------------------------
    # APPLY
    # --------------------------------------

    if st.button(
        "Apply my changes →",
        type="primary"
    ):

        approved_suggestions = (
            selected_priority
            + selected_rewrites
        )


        if not approved_suggestions:

            st.warning(
                "Select at least one change first."
            )


        else:

            with st.spinner(
                "Updating your CV..."
            ):

                try:

                    updated_cv = apply_suggestions(
                        cv_data,
                        approved_suggestions
                    )

                    st.session_state[
                        "updated_cv"
                    ] = updated_cv

                    st.success(
                        "Your selected changes have been applied."
                    )


                except Exception as e:

                    st.error(
                        f"Could not update the CV: {e}"
                    )


# ==========================================
# REFINED CV
# ==========================================

if "updated_cv" in st.session_state:

    updated_cv = st.session_state[
        "updated_cv"
    ]


    st.divider()

    st.header(
        "Your Refined CV"
    )

    st.caption(
        "Preview the updated content before creating your final PDF."
    )


    # --------------------------------------
    # SUMMARY
    # --------------------------------------

    st.subheader(
        "Professional Summary"
    )

    with st.container(border=True):

        st.write(
            updated_cv.summary
        )


    # --------------------------------------
    # SKILLS
    # --------------------------------------

    st.subheader(
        "Skills"
    )

    with st.container(border=True):

        if updated_cv.skills:

            st.write(
                "  •  ".join(
                    updated_cv.skills
                )
            )

        else:

            st.caption(
                "No skills listed."
            )


    # --------------------------------------
    # EXPERIENCE
    # --------------------------------------

    st.subheader(
        "Experience"
    )


    for experience in updated_cv.experience:

        with st.container(border=True):

            st.markdown(
                f"### {experience.role}"
            )

            company_text = experience.company

            if experience.duration:

                company_text += (
                    f"  •  {experience.duration}"
                )

            st.caption(
                company_text
            )


            for responsibility in (
                experience.responsibilities
            ):

                st.write(
                    f"• {responsibility}"
                )


    # --------------------------------------
    # PROJECTS
    # --------------------------------------

    st.subheader(
        "Projects"
    )


    for project in updated_cv.projects:

        with st.container(border=True):

            st.markdown(
                f"### {project.title}"
            )

            st.write(
                project.description
            )


            if project.technologies:

                st.caption(
                    " • ".join(
                        project.technologies
                    )
                )


    # --------------------------------------
    # FINAL PDF
    # --------------------------------------

    st.divider()

    st.subheader(
        "Create your final CV"
    )

    st.caption(
        "Generate a polished PDF from the refined content above."
    )


    if st.button(
        "Create Final CV →",
        type="primary"
    ):

        with st.spinner(
            "Creating your CV..."
        ):

            try:

                output_path = generate_cv_pdf(
                    updated_cv
                )

                st.session_state[
                    "generated_pdf"
                ] = output_path

                st.success(
                    "Your final CV is ready."
                )


            except Exception as e:

                st.error(
                    f"PDF generation failed: {e}"
                )


# ==========================================
# DOWNLOAD
# ==========================================

if "generated_pdf" in st.session_state:

    pdf_path = st.session_state[
        "generated_pdf"
    ]


    st.divider()

    with st.container(border=True):

        st.subheader(
            "Your CV is ready"
        )

        st.caption(
            "Download the refined version and use it for your next application."
        )


        with open(
            pdf_path,
            "rb"
        ) as pdf_file:

            st.download_button(
                label="Download CV ↓",
                data=pdf_file,
                file_name="CVGlowUp_Improved_CV.pdf",
                mime="application/pdf"
            )