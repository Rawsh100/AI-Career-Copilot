import streamlit as st
import os
import sys

# allow import from core folder
sys.path.append(os.path.abspath("core"))

from resume_analyzer import analyze_resume


st.title("🚀 AI Career Copilot")

st.write("Upload Resume and Get AI HR Feedback")


uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)


if uploaded_file is not None:

    save_path = "data/resumes/resume.pdf"

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Resume Uploaded Successfully")


    if st.button("Analyze Resume"):

        st.write("Analyzing Resume...")

        result = analyze_resume()

        st.write(result)