import streamlit as st
import fitz  # PyMuPDF
import docx
import pytesseract
from pdf2image import convert_from_bytes
from PIL import Image
from gpt_matcher import get_match_score

st.title("Resume Optimizer - Upload Step")

resume_file = st.file_uploader("Upload your Resume (PDF or DOCX)", type=["pdf", "docx"])
jd_file = st.file_uploader("Upload Job Description (PDF or DOCX)", type=["pdf", "docx"])


def extract_text_from_pdf(uploaded_file):
    try:
        # Attempt standard PDF text extraction
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
            text = ""
            for page in doc:
                text += page.get_text()
        if text.strip():
            return text
    except Exception as e:
        print("⚠️ PyMuPDF failed:", e)

    # OCR fallback
    uploaded_file.seek(0)  # Reset pointer for OCR
    images = convert_from_bytes(uploaded_file.read())
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img)
    return text


def extract_text_from_docx(uploaded_file):
    try:
        doc = docx.Document(uploaded_file)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        print("⚠️ DOCX extraction failed:", e)
        return ""


def extract_text(file):
    if file.name.endswith(".pdf"):
        return extract_text_from_pdf(file)
    elif file.name.endswith(".docx"):
        return extract_text_from_docx(file)
    else:
        return ""


if resume_file and jd_file:
    resume_text = extract_text(resume_file)
    jd_text = extract_text(jd_file)

    st.subheader("Resume Text Preview")
    st.text_area("Resume Content", resume_text[:2000], height=300)

    st.subheader("Job Description Text Preview")
    st.text_area("JD Content", jd_text[:2000], height=300)

    if st.button("Next Step"):
        if not resume_text.strip() or not jd_text.strip():
            st.warning("One or both files seem to have no text. Please check the file contents.")
        else:
            with st.spinner("Analyzing with GPT..."):
                result = get_match_score(resume_text, jd_text)

            st.subheader("🔍 GPT Match Analysis")
            st.markdown(result)
