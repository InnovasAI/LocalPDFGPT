# 🧠 Chat With Your PDF (Locally, Using RAG + Ollama + LangChain)

A private, local AI assistant that lets you chat with your own PDF files using **retrieval-augmented generation (RAG)** and **local large language models** (LLMs) via [Ollama](https://ollama.com/). No internet or API keys required!

This project loads a PDF (e.g., `book.pdf`), splits it into chunks, creates embeddings using a local model (`llama3.2`), stores them in a vector database (Chroma), and lets you ask questions interactively via CLI or web interface.

---

## 🚀 Features

- 🔒 100% local, private, and offline
- 🧠 Uses your own PDF files as context
- 📦 Powered by [LangChain](https://www.langchain.com/), [ChromaDB](https://www.trychroma.com/), and [Ollama](https://ollama.com/)
- 🗣️ Chat via terminal (CLI interface)
- 🌐 Modern web chat interface with formatting support
- 💾 Automatic chat history saving and export
- 📱 Responsive design for desktop and mobile
- ⚡ Fast inference with `llama3.2` running locally

---

## 🧰 Tech Stack

- [Python 3.10+](https://www.python.org/)
- [Ollama](https://ollama.com/) (for running the LLM locally)
- LangChain
- ChromaDB (for vector storage)
- Flask (for web interface)
- Llama 3.2 (via `llama3.2:latest` model)

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

Then pull the Llama model:
```bash
ollama pull llama3.2:latest
```

### 4. Run the Application

You can now use the convenient startup script:

```bash
python start.py
```

This will give you options to:
1. 🖥️ Use the Command Line Interface
2. 🌐 Start the Web Interface
3. 📊 Load and Index your PDF (first time setup)

### Alternative: Direct Usage

**First time setup - Index your PDF:**
```bash
python load_and_index.py
```

**Use CLI interface:**
```bash
python chat_cli.py
```

**Use Web interface:**
```bash
python web_chat.py
```
The system will automatically find an available port (starting from 8080) and display the URL to open in your browser.

---

## 🌐 Web Interface Features

- **Modern Chat UI**: Clean, responsive design that works on desktop and mobile
- **Text Formatting**: Supports markdown formatting including code blocks, tables, lists
- **Chat History**: Automatically saves all conversations
- **Export Function**: Download your chat history as JSON
- **Real-time Status**: Shows connection status and model information
- **Keyboard Shortcuts**: Enter to send, Shift+Enter for new lines

---

## 📁 Files Overview

| File | Purpose |
|------|---------|
| `load_and_index.py` | Loads the PDF, splits it, creates vector DB |
| `chat_cli.py` | Interactive command-line chat interface |
| `web_chat.py` | Flask web server for browser-based chat |
| `chat_engine.py` | Shared chat logic used by both interfaces |
| `start.py` | Convenient startup script with menu options |
| `templates/index.html` | Web interface HTML template |
| `book.pdf` | Your source document for Q&A |

---

## 🧠 How It Works

1. �️ PDF loaded with PyPDFLoader
2. 📄 Split into chunks using RecursiveCharacterTextSplitter
3. 💡 Embedded using Ollama's local llama3.2
4. 🧭 Stored in Chroma vector DB
5. ❓ Query gets matched with relevant chunks
6. 🧠 Answer generated with local Llama LLM using context

---

## 💾 Chat History

Both CLI and web interfaces automatically save your chat history:
- History is saved to `chat_history.json`
- Web interface allows you to export conversations
- View previous conversations when you restart
- Clear history option available

---

## 🔧 Customization

You can easily customize the setup:

- **Change PDF file**: Replace `book.pdf` with your document
- **Switch models**: Update the model name in the chat files
- **Adjust chunk size**: Modify parameters in `load_and_index.py`
- **Web interface styling**: Edit `templates/index.html`

---
---

## 🚀 Quick Start

1. Place your PDF file as `book.pdf` in the project directory
2. Run `python start.py` and choose option 3 to index your PDF
3. Choose option 1 for CLI or option 2 for web interface
4. Start asking questions about your PDF!

---

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

---

## � License

This project is licensed under the MIT License - see the LICENSE file for details.
