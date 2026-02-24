# 🚀 AI Career Copilot — Resume Analyzer + RAG Chatbot (FREE Llama3 Version)

AI Career Copilot is a Generative AI Resume Assistant built using Retrieval Augmented Generation (RAG).

This version runs completely locally using Llama3 via Ollama.

No OpenAI billing or API key required.

---

## ⭐ Features

- Resume PDF Analysis
- Resume Question Answering Chatbot
- Local LLM (Llama3)
- FAISS Vector Database
- Streamlit Web UI.

---

## 🛠 Tech Stack

- Python
- LangChain
- Ollama (Llama3)
- HuggingFace Embeddings
- FAISS
- Streamlit.

---

## ⚙️ Setup Instructions

Clone repository:


git clone https://github.com/Rawsh100/AI-Career-Copilot.git


Go inside folder:


cd AI-Career-Copilot


---

### Create Virtual Environment


python -m venv venv


Activate (Windows):


.\venv\Scripts\activate


---

### Install Dependencies


pip install -r requirements.txt


---

## 🧠 Install Ollama (Required)

Download:

https://ollama.com/download

Verify installation:


ollama --version


---

## ⬇️ Download Llama3 Model


ollama pull llama3


---

## ▶️ Run Resume Chatbot

Start Ollama:


ollama run llama3


In another terminal:


python core/resume_chatbot.py


---

## 🌐 Run Web UI


streamlit run frontend/chat_app.py


Open:


http://localhost:8501


---

## 🎯 Skills Demonstrated

- Generative AI
- Retrieval Augmented Generation (RAG)
- Local LLM Deployment
- Vector Databases
- Prompt Engineering.

---

## 👩‍💻 Author

Shweta Rawat

GitHub:

https://github.com/Rawsh100