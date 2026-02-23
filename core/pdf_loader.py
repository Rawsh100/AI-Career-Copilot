from langchain_community.document_loaders import PyPDFLoader
import os

def load_resume():

    base_dir = os.path.dirname(os.path.dirname(__file__))

    path = os.path.join(
        base_dir,
        "data",
        "resumes",
        "resume.pdf"
    )

    loader = PyPDFLoader(path)

    docs = loader.load()

    return docs