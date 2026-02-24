🚀 AI Career Copilot — Resume Analyzer + RAG Chatbot (FREE Local AI Version)

AI Career Copilot is a Generative AI Resume Assistant powered by Retrieval Augmented Generation (RAG).

It analyzes resumes and allows intelligent question answering using a completely FREE local Large Language Model (LLM) running via Ollama.

✅ No OpenAI Billing
✅ No API Keys Required
✅ Runs Fully Offline.

⭐ Features

Resume PDF Analysis

Resume Question Answering Chatbot

Resume Knowledge Base Creation

Local LLM Powered Responses

Streamlit Web Interface.

🛠 Tech Stack

Python

LangChain

Ollama (Phi3 Mini — Local LLM)

FAISS Vector Database

PDF Processing

Streamlit UI.

⚙️ Setup Instructions

Clone repository:

git clone https://github.com/Rawsh100/AI-Career-Copilot.git

Go inside project:

cd AI-Career-Copilot
🐍 Create Virtual Environment
python -m venv venv

Activate (Windows):

.\venv\Scripts\activate
📦 Install Dependencies
pip install -r requirements.txt
🧠 Install Ollama (Required)

Download Ollama:

https://ollama.com/download

Verify installation:

ollama --version
⬇️ Download FREE Local AI Model

Install lightweight model (recommended for low RAM systems):

ollama pull phi3:mini
▶️ Run Resume Chatbot (Terminal Mode)

Start Ollama server:

ollama serve

In another terminal:

python core/resume_chatbot.py
🌐 Run Web UI (Recommended)

Start Streamlit:

streamlit run frontend/chat_app.py

Open browser:

http://localhost:8506/
🎯 Skills Demonstrated

Generative AI

Retrieval Augmented Generation (RAG)

Vector Databases (FAISS)

Local LLM Deployment

Prompt Engineering

Resume Intelligence Systems.

📂 Project Structure
AI-Career-Cilot
│
├── core
│ ├── pdf_loader.py
│ ├── chunker.py
│ ├── vectorstore.py
│ └── resume_chatbot.py
│
├── data
│ └── resumes
│
├── frontend
│ └── chat_app.py
│
├── vectorstore
├── requirements.txt
└── README.md
👩‍💻 Author

Shweta Rawat

GitHub:

https://github.com/Rawsh100

⭐ Why This Project?

This project demonstrates real-world usage of:

Resume Intelligence Systems

Enterprise RAG Pipelines

Local AI Deployment

End-to-End LLM Application Development.