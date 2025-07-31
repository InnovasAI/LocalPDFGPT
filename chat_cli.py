# chat_cli.py
from langchain.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama

# Load vector store
embedding = OllamaEmbeddings(model="mistral-nemo")
vectorstore = Chroma(persist_directory="./db", embedding_function=embedding)
retriever = vectorstore.as_retriever()

# Load local LLM
llm = Ollama(model="mistral-nemo")

# Create RAG QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=False  # Change to True if you want sources
)

# Chat loop
print("🤖 Ask me anything about the company (type 'exit' to quit)")
while True:
    query = input("\n> ")
    if query.lower() in ['exit', 'quit']:
        break
    response = qa_chain({"query": query})
    print("\nAnswer:\n", response['result'])
