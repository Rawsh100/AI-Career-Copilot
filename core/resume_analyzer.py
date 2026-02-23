import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

env_path = os.path.join(BASE_DIR, ".env")

print("ENV PATH:", env_path)

load_dotenv(env_path)

print("KEY =", os.getenv("OPENAI_API_KEY"))
import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from pdf_loader import load_resume


# ---------- Load .env from project root ----------

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

env_path = os.path.join(BASE_DIR, ".env")

load_dotenv(env_path)


def analyze_resume():

    # ---------- Load API KEY ----------

    api_key = os.getenv("OPENAI_API_KEY")

    print("API KEY FOUND :", api_key is not None)

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY not found. Check .env file location."
        )

    # ---------- Load Resume ----------

    docs = load_resume()

    resume_text = ""

    for doc in docs:
        resume_text += doc.page_content + "\n"


    # ---------- GPT Model ----------

    llm = ChatOpenAI(
        api_key=api_key,
        model="gpt-4o-mini",
        temperature=0
    )


    # ---------- Prompt ----------

    prompt = f"""
You are a Senior HR Recruiter.

Analyze this resume carefully.

Give:

1. Resume Score out of 10
2. Strengths
3. Weaknesses
4. Missing Skills
5. Improvement Suggestions.

Resume:

{resume_text}
"""


    # ---------- Call GPT ----------

    response = llm.invoke(prompt)


    print("\n========= RESUME ANALYSIS =========\n")

    return response.content



# ---------- Run Program ----------

if __name__ == "__main__":
    print("🔥 MAIN EXECUTING")
    analyze_resume()