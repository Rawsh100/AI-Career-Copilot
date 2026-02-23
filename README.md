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
