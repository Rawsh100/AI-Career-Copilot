from langchain.chat_models import ChatOpenAI

def analyze_resume(context):

    llm = ChatOpenAI(temperature=0)

    prompt=f"""
You are HR expert.

Score resume.

Suggest improvements.

Resume:

{context}
"""

    return llm.predict(prompt)
