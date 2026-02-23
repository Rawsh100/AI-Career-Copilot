import streamlit as st

st.title("AI Career Copilot")

tab1,tab2,tab3=st.tabs(
["Resume","Interview","Q&A"]
)

with tab1:

 st.write("Resume Analyzer")

with tab2:

 st.write("Interview Practice")

with tab3:

 st.write("Document QA")