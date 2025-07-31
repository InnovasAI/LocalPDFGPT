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
        self.vectorstore = Chroma(persist_directory="./db", embedding_function=self.embedding)
        self.retriever = self.vectorstore.as_retriever()
        self.llm = Ollama(model=model_name)
        
        # Create RAG QA chain
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=self.retriever,
            return_source_documents=False
        )
        
        # Initialize chat history
        self.chat_history = []
        self.chat_history_file = "./chat_history.json"
        self.load_chat_history()
    
    def get_response(self, query):
        """Get response from the RAG chain"""
        try:
            response = self.qa_chain({"query": query})
            result = response['result']
            
            # Add to chat history
            self.add_to_history(query, result)
            
            return result
        except Exception as e:
            error_msg = f"Error processing query: {str(e)}"
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
