from langchain.chat_models import ChatOpenAI

def ask_question(context,question):

    llm=ChatOpenAI()

    prompt=f"""
Answer ONLY using context.

Context:

{context}

Question:

{question}
"""

    return llm.predict(prompt)