# 🚀 AI Career Copilot — Resume Analyzer + RAG Chatbot

AI Career Copilot is a Generative AI application that analyzes resumes and allows users to chat with their resume using Retrieval Augmented Generation (RAG).

The project demonstrates practical usage of LLMs, embeddings, vector databases, and conversational AI.

---

## ⭐ Features

### ✅ Resume Analyzer

- Upload resume PDF
- AI HR evaluation using GPT
- Resume score and feedback
- Strengths and weaknesses analysis.

---

### ✅ Resume Chatbot (RAG)

Ask questions like:

- What skills does the candidate have?
- Generate interview questions.
- What experience is mentioned?

Uses vector search to generate grounded responses.

---

### ✅ Web UI

Built using Streamlit.

- Upload Resume
- Build Knowledge Base
- Chat with Resume.

---

## 🧠 Architecture

PDF Resume  
↓  
Document Loader  
↓  
Chunking  
↓  
OpenAI Embeddings  
↓  
FAISS Vector Database  
↓  
Retriever  
↓  
GPT Response.

---

## 🛠 Tech Stack

- Python
- OpenAI GPT Models
- LangChain
- FAISS Vector Database
- Streamlit
- RAG Architecture

---

## 📂 Project Structure

AI-Career-Copilot

core → Backend logic

frontend → Streamlit UI

data → Resume files

vectorstore → FAISS database

---

## ⚙️ Setup Instructions

Clone repository:

----
git clone https://github.com/Rawsh100/AI-Career-Copilot.git


Go inside the project folder:

---

### Create Virtual Environment

python -m venv venv

---

### Activate Environment

Windows:

.\venv\Scripts\activate

---

### Install Dependencies


pip install -r requirements.txt


---

### Create `.env` File

Add your OpenAI API key:


OPENAI_API_KEY=your_api_key_here


---

## ▶️ Run Resume Analyzer


python core/resume_analyzer.py


---

## ▶️ Run Resume Chatbot (RAG)


python core/resume_chatbot.py


---

## 🌐 Run Web UI


streamlit run frontend/chat_app.py


Open browser:


http://localhost:8501


---

## 🎯 Skills Demonstrated

- Generative AI
- Retrieval Augmented Generation (RAG)
- Vector Databases
- Prompt Engineering
- LLM Integration

---

## 👩‍💻 Author

Shweta Rawat

GitHub:

https://github.com/Rawsh100