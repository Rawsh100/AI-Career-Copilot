from dotenv import load_dotenv
import os

load_dotenv()

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def create_vectorstore(chunks):

    embeddings = OpenAIEmbeddings()

    db = FAISS.from_documents(
        chunks,
        embeddings
    )

    db.save_local("vectorstore/resume")

    return db