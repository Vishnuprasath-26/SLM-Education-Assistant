models = [
    {
        "name": "Qwen2.5-0.5B-Instruct",
        "model_id": "Qwen/Qwen2.5-0.5B-Instruct",
        "parameters": "0.49B",
        "context_length": "32K tokens",
        "license": "Apache 2.0",
        "capabilities": "Instruction following, text generation, question answering",
        "hardware": "Low resource requirement compared with larger candidates",
        "suitability": "Good candidate for CPU-based education assistant"
    },
    {
        "name": "Phi-3.5-mini-instruct",
        "model_id": "microsoft/Phi-3.5-mini-instruct",
        "parameters": "3.8B",
        "context_length": "128K tokens",
        "license": "MIT",
        "capabilities": "Reasoning, mathematics, coding, multilingual text",
        "hardware": "High memory requirement for local CPU inference",
        "suitability": "Powerful but demanding for our hardware"
    },
    {
        "name": "Gemma-3-1B-it",
        "model_id": "google/gemma-3-1b-it",
        "parameters": "1B",
        "context_length": "32K tokens",
        "license": "Gemma Terms of Use",
        "capabilities": "Instruction following, question answering, text generation",
        "hardware": "Moderate resource requirement",
        "suitability": "Good lightweight education assistant candidate"
    }
]

for model in models:
    print("\n" + "=" * 60)
    for key, value in model.items():
        print(f"{key}: {value}")