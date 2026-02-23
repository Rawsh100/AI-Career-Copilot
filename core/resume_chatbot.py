import os
from dotenv import load_dotenv

from pdf_loader import load_resume
from chunker import chunk_docs
from vectorstore import create_vectorstore

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

from langchain_community.vectorstores import FAISS


# ---------- Load .env ----------

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

load_dotenv(os.path.join(BASE_DIR, ".env"))


# ---------- Build Knowledge Base ----------

def build_chatbot():

    print("Loading Resume...")

    docs = load_resume()

    print("Chunking Resume...")

    chunks = chunk_docs(docs)

    print("Creating Vector Database...")

    create_vectorstore(chunks)

    print("Knowledge Base Ready ✅")



# ---------- Ask Questions ----------

def ask_resume(question):

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in .env")

    # OpenAI Embeddings (NO TORCH)
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    # Load FAISS DB
    db = FAISS.load_local(
        "vectorstore/resume_db",
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = db.as_retriever(search_kwargs={"k":3})

    docs = retriever.get_relevant_documents(question)

    context = ""

    for doc in docs:
        context += doc.page_content + "\n"


    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    prompt = f"""
You are an expert HR recruiter.

Answer ONLY using the resume context below.

Resume Context:

{context}

Question:

{question}
"""

    response = llm.invoke(prompt)

    print("\n===== ANSWER =====\n")

    return response.content



# ---------- Main ----------

if __name__ == "__main__":

    print("Building Resume Knowledge Base...")

    build_chatbot()

    while True:

        q = input("\nAsk Resume Question (type exit to stop): ")

        if q.lower() == "exit":
            break

        ask_resume(q)