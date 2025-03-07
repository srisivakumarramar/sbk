from langchain_community.chat_models import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

def customer_support_bot(user_query):
    # Initialize Ollama model
    chat = ChatOllama(model="mistral")  # You can use other Ollama models like 'llama2' or 'gemma'
    
    # Define conversation context
    system_message = SystemMessage(content="You are a helpful AI assistant for customer support. Respond accurately and professionally.")
    user_message = HumanMessage(content=user_query)
    
    # Get response from Ollama
    response = chat([system_message, user_message])
    
    return response.content

# Example real-time usage
if __name__ == "__main__":
    while True:
        query = input("Customer: ")
        if query.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        response = customer_support_bot(query)
        print("Support AI:", response)
