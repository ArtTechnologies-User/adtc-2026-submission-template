from llama_cpp import Llama

llm = Llama(model_path="models/llama-2-7b-chat-hf-q4_k_m.gguf")

while True:
    question = input("Enter your WAEC question (or 'quit' to exit): ")
    if question.lower() == "quit":
        break
    output = llm(f"Q: {question}\nA:", max_tokens=200)
    print("Answer:", output["choices"][0]["text"])


