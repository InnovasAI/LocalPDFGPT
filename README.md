# 🧠 Chat With Your PDF (Locally, Using RAG + Ollama + LangChain)

A private, local AI assistant that lets you chat with your own PDF files using **retrieval-augmented generation (RAG)** and **local large language models** (LLMs) via [Ollama](https://ollama.com/). No internet or API keys required!

This project loads a PDF (e.g., `company_fines.pdf`), splits it into chunks, creates embeddings using a local model (`mistral-nemo`), stores them in a vector database (Chroma), and lets you ask questions interactively from the terminal.

---

## 🚀 Features

- 🔒 100% local, private, and offline
- 🧠 Uses your own PDF files as context
- 📦 Powered by [LangChain](https://www.langchain.com/), [ChromaDB](https://www.trychroma.com/), and [Ollama](https://ollama.com/)
- 🗣️ Chat via terminal (CLI interface)
- ⚡ Fast inference with `mistral-nemo` running locally

---

## 🧰 Tech Stack

- [Python 3.10+](https://www.python.org/)
- [Ollama](https://ollama.com/) (for running the LLM locally)
- LangChain
- ChromaDB (for vector storage)
- Mistral (via `mistral-nemo:latest` model)

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/chat-with-your-pdf.git
cd chat-with-your-pdf
```
### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Download and Start Ollama + Model
Make sure Ollama is installed and running.

Then pull the Mistral model:
```bash
ollama pull mistral-nemo:latest
```

## 📁 Files Overview
### File	Purpose
- load_and_index.py	Loads the PDF, splits it, creates vector DB
- chat_cli.py	Interactive command-line chat interface
- company_fines.pdf	Your source document for Q&A

🧠 How It Works
🗃️ PDF loaded with PyPDFLoader

- 📄 Split into chunks using RecursiveCharacterTextSplitter
- 💡 Embedded using Ollama's local mistral-nemo
- 🧭 Stored in Chroma vector DB
- ❓ Query gets matched with relevant chunks
- 🧠 Answer generated with local Mistral LLM using context
