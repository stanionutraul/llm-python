import requests
import sys

sys.stdout.reconfigure(encoding="utf-8")

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3.2",
        "prompt": "Salut! Cine ești?",
        "stream": False
    }
)

print(response)
print(response.json()["response"])