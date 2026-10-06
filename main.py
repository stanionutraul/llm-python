import requests
import sys

sys.stdout.reconfigure(encoding="utf-8")

def ask_llm(prompt: str):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]

history = []

while True:
    prompt = input("Enter your prompt (or type 'exit' to quit): ")
    if prompt.lower() == 'exit':
        print("La revedere!")
        break

    history.append(f"User: {prompt}") 

    conversation = "\n".join(history)
    conversation += "\nAssistant:"



    response = ask_llm(conversation)

    history.append(f"Assistant: {response}")
    print("Llama:", response)
