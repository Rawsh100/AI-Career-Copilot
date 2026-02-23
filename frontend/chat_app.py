import streamlit as st
import os
import sys

# allow import from core folder
sys.path.append(os.path.abspath("core"))

from resume_chatbot import build_chatbot, ask_resume


st.title("🚀 AI Career Copilot — Resume Chatbot")

st.write("Upload Resume and Chat with AI")


# ---------- Upload Resume ----------

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)


if uploaded_file:

    save_path = "data/resumes/resume.pdf"

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Resume Uploaded!")

    if st.button("Build Knowledge Base"):

        build_chatbot()

        st.success("Knowledge Base Ready!")


# ---------- Chat Section ----------

question = st.text_input("Ask Question About Resume")


if st.button("Ask"):

    if question:

        st.write("Thinking...")

        answer = ask_resume(question)

        st.write(answer)