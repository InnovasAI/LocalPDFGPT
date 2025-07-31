# chat_cli.py
from chat_engine import ChatEngine

# Initialize chat engine
chat_engine = ChatEngine(model_name="llama3.2:latest")

# Chat loop
print("🤖 Ask me anything about the PDF (type 'exit' to quit)")
print("💾 Chat history is automatically saved to chat_history.json")
while True:
    query = input("\n> ")
    if query.lower() in ['exit', 'quit']:
        break
    response = chat_engine.get_response(query)
    print("\nAnswer:\n", response)
