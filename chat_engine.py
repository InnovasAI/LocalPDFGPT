# chat_engine.py
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama
import json
import os
from datetime import datetime


class ChatEngine:
    def __init__(self, model_name="llama3.2:latest"):
        self.model_name = model_name
        self.embedding = OllamaEmbeddings(model=model_name)
        self.vectorstore = Chroma(
            persist_directory="./db", embedding_function=self.embedding)
        self.retriever = self.vectorstore.as_retriever()
        self.llm = Ollama(model=model_name)

        # Create RAG QA chain with custom prompt
        from langchain.prompts import PromptTemplate

        template = """You are a helpful AI assistant that answers questions based on the provided PDF document content. 
        Always use the context from the PDF to answer questions. If the context doesn't contain relevant information, 
        say "I don't see that specific information in the PDF document I have access to" but still try to provide 
        helpful information based on what IS in the PDF.

        Context from PDF: {context}

        Question: {question}

        Answer based on the PDF content:"""

        QA_CHAIN_PROMPT = PromptTemplate(
            input_variables=["context", "question"],
            template=template,
        )

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=self.retriever,
            return_source_documents=False,
            chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
        )

        # Initialize chat history
        self.chat_history = []
        self.chat_history_file = "./chat_history.json"
        self.load_chat_history()

    def get_response(self, query):
        """Get response from the RAG chain"""
        try:
            # First, let's test if we can retrieve documents
            docs = self.retriever.get_relevant_documents(query)
            print(f"🔍 Retrieved {len(docs)} documents for query: {query}")

            if len(docs) == 0:
                return "I don't have access to any PDF content. Please make sure a PDF has been indexed first using the 'Load and Index PDF' option."

            # Show some context from retrieved docs for debugging
            for i, doc in enumerate(docs[:2]):  # Show first 2 docs
                print(f"📄 Doc {i+1}: {doc.page_content[:100]}...")

            response = self.qa_chain({"query": query})
            result = response['result']

            # Add to chat history
            self.add_to_history(query, result)

            return result
        except Exception as e:
            error_msg = f"Error processing query: {str(e)}"
            print(f"❌ {error_msg}")
            self.add_to_history(query, error_msg)
            return error_msg

    def add_to_history(self, query, response):
        """Add query and response to chat history"""
        chat_entry = {
            "timestamp": datetime.now().isoformat(),
            "query": query,
            "response": response
        }
        self.chat_history.append(chat_entry)
        self.save_chat_history()

    def save_chat_history(self):
        """Save chat history to file"""
        try:
            with open(self.chat_history_file, 'w', encoding='utf-8') as f:
                json.dump(self.chat_history, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Warning: Could not save chat history: {e}")

    def load_chat_history(self):
        """Load chat history from file"""
        try:
            if os.path.exists(self.chat_history_file):
                with open(self.chat_history_file, 'r', encoding='utf-8') as f:
                    self.chat_history = json.load(f)
        except Exception as e:
            print(f"Warning: Could not load chat history: {e}")
            self.chat_history = []

    def get_chat_history(self):
        """Get the full chat history"""
        return self.chat_history

    def clear_chat_history(self):
        """Clear the chat history"""
        self.chat_history = []
        self.save_chat_history()

    def export_chat_history(self, filename=None):
        """Export chat history to a file"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"chat_export_{timestamp}.json"

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.chat_history, f, indent=2, ensure_ascii=False)
            return filename
        except Exception as e:
            raise Exception(f"Could not export chat history: {e}")
