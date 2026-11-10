
import time
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma3:1b"

question = "What is Machine Learning? Explain with three real-life examples."

payload = {
    "model": MODEL_NAME,
    "prompt": question,
    "stream": False,
    "options": {
        "temperature": 0,
        "num_predict": 150
    }
}

print("Sending question to Gemma...")

start_time = time.time()

response = requests.post(
    OLLAMA_URL,
    json=payload,
    timeout=180
)

end_time = time.time()

response.raise_for_status()

result = response.json()

answer = result["response"]
total_time = end_time - start_time
generated_tokens = result["eval_count"]
generation_time = result["eval_duration"] / 1_000_000_000

print("\nQuestion:", question)
print("\nGemma Answer:\n", answer)

print("\n--- Performance Metrics ---")
print("Total response time:", round(total_time, 2), "seconds")
print("Generated tokens:", generated_tokens)
print("Generation time:", round(generation_time, 2), "seconds")
print("Tokens per second:", round(generated_tokens / generation_time, 2))
print("Model:", MODEL_NAME)
