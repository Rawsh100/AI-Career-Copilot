from langchain.chat_models import ChatOpenAI

def evaluate_answer(question,answer):

    llm=ChatOpenAI()

    prompt=f"""
Act as strict interviewer.

Question:

{question}

Answer:

{answer}

Give:

Score out of 10

Strength

Improvements
"""

    return llm.predict(prompt)