from langchain_community.llms import Ollama

# Initialize the Ollama model
llm = Ollama(model="mistral")  # Mistral is optimized for speed

# Function to get quick responses
def quick_faq_bot(question):
    prompt = f"Answer this in one sentence: {question}"
    return llm.invoke(prompt)  # Faster response generation

# Example use case
if __name__ == "__main__":
    while True:
        query = input("Ask a question (or type 'exit' to quit): ")
        if query.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        print("Bot:", quick_faq_bot(query))
