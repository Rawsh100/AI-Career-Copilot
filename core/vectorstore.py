from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings


def create_vectorstore(chunks):

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    db = FAISS.from_documents(
        chunks,
        embeddings
    )

    db.save_local("vectorstore/resume_db")

    return db