# load_and_index.py
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings

# Load and split PDF
loader = PyPDFLoader("company_file.pdf")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.split_documents(documents)

# Generate embeddings and create vector store
embedding = OllamaEmbeddings(model="mistral-nemo")
vectorstore = Chroma.from_documents(
    docs,
    embedding=embedding,
    persist_directory="./db"
)

vectorstore.persist()
print("✅ Vector store created and saved to ./db")
