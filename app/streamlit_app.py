import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="CVGlowUp",
    page_icon="✨",
    layout="wide"
)

html = """
<!DOCTYPE html>
<html>
<head>
<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #f7f8fc;
}

.hero {
    height: 620px;
    position: relative;
    overflow: hidden;
    border-radius: 28px;
    background: linear-gradient(
        110deg,
        #ffffff 0%,
        #f5f6ff 55%,
        #e8eaf3 100%
    );
    padding: 65px;
    box-shadow: 0 15px 50px rgba(30,35,60,0.08);
}

.hero-content {
    position: relative;
    z-index: 10;
    width: 52%;
}

.logo {
    font-size: 25px;
    font-weight: 700;
    margin-bottom: 75px;
    color: #202333;
}

.hero-title {
    font-size: 60px;
    font-weight: 750;
    line-height: 1.05;
    letter-spacing: -2px;
    color: #171923;
}

.hero-title span {
    color: #635bff;
}

.hero-text {
    font-size: 18px;
    color: #666b7a;
    max-width: 520px;
    line-height: 1.6;
    margin-top: 24px;
}


/* OFFICE */

.office {
    position: absolute;
    right: -10px;
    top: 0;
    width: 55%;
    height: 100%;
    opacity: 0.25;
}


/* WINDOW */

.window {
    position: absolute;
    right: 60px;
    top: 50px;
    width: 340px;
    height: 250px;
    border: 8px solid #969baa;
    background: #dfe4ef;
}

.window-v {
    position: absolute;
    left: 50%;
    top: 0;
    width: 5px;
    height: 100%;
    background: #aeb4c1;
}

.window-h {
    position: absolute;
    left: 0;
    top: 50%;
    width: 100%;
    height: 5px;
    background: #aeb4c1;
}


/* MANAGER */

.manager-head {
    position: absolute;
    right: 280px;
    top: 125px;
    width: 80px;
    height: 80px;
    border-radius: 50%;
    background: #707686;
}

.manager-body {
    position: absolute;
    right: 215px;
    top: 195px;
    width: 200px;
    height: 190px;
    border-radius: 85px 85px 15px 15px;
    background: #5c6373;
}

.arm {
    position: absolute;
    right: 180px;
    top: 275px;
    width: 165px;
    height: 26px;
    border-radius: 20px;
    background: #505666;
    transform: rotate(15deg);
}


/* DESK */

.desk {
    position: absolute;
    right: 45px;
    bottom: 95px;
    width: 520px;
    height: 30px;
    background: #505666;
    border-radius: 6px;
}

.desk-leg {
    position: absolute;
    right: 120px;
    bottom: 0;
    width: 22px;
    height: 105px;
    background: #505666;
}


/* CV */

.cv-paper {
    position: absolute;
    right: 165px;
    top: 260px;
    width: 110px;
    height: 150px;
    background: white;
    border-radius: 5px;
    transform: rotate(-12deg);
    box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    padding-top: 1px;
}

.cv-line {
    height: 5px;
    background: #b8bdc8;
    margin: 14px 12px 0;
    border-radius: 3px;
}

.cv-line.small {
    width: 55%;
}


/* LAPTOP */

.laptop {
    position: absolute;
    right: 315px;
    bottom: 125px;
    width: 150px;
    height: 88px;
    background: #363b49;
    border-radius: 8px;
    padding: 9px;
}

.laptop-screen {
    width: 100%;
    height: 100%;
    background: #e9ebf4;
    border-radius: 4px;
}

</style>
</head>

<body>

<div class="hero">

    <div class="hero-content">

        <div class="logo">
            ✨ CVGlowUp
        </div>

        <div class="hero-title">
            Make your CV<br>
            <span>stand out.</span>
        </div>

        <div class="hero-text">
            Upload your CV and let AI analyze, review
            and improve it like a senior hiring manager.
        </div>

    </div>


    <div class="office">

        <div class="window">
            <div class="window-v"></div>
            <div class="window-h"></div>
        </div>

        <div class="manager-head"></div>

        <div class="manager-body"></div>

        <div class="arm"></div>

        <div class="cv-paper">
            <div class="cv-line"></div>
            <div class="cv-line"></div>
            <div class="cv-line small"></div>
            <div class="cv-line"></div>
            <div class="cv-line small"></div>
        </div>

        <div class="desk"></div>

        <div class="desk-leg"></div>

        <div class="laptop">
            <div class="laptop-screen"></div>
        </div>

    </div>

</div>

</body>
</html>
"""

components.html(html, height=640, scrolling=False)


# ==============================
# UPLOAD
# ==============================

st.markdown("## 📄 Upload your CV")
st.caption("PDF or DOCX • Max 200MB")

uploaded_file = st.file_uploader(
    "Choose your CV",
    type=["pdf", "docx"],
    label_visibility="collapsed"
)

if uploaded_file:
    st.success(f"✓ {uploaded_file.name} uploaded successfully")