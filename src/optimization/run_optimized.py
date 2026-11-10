
import json
import time
from pathlib import Path

import requests

CONFIG_PATH = Path("configs/optimized_config.json")
QUESTIONS_PATH = Path("data/evaluation/baseline_questions.jsonl")
OUTPUT_PATH = Path("data/evaluation/optimized_results.jsonl")


def load_config():
    with CONFIG_PATH.open("r", encoding="utf-8-sig") as file:
        return json.load(file)


def load_questions():
    questions = []

    with QUESTIONS_PATH.open("r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                questions.append(json.loads(line))

    return questions


def generate_answer(question, config):

    instructions = "\n".join(
        f"{index}. {instruction}"
        for index, instruction in enumerate(
            config["prompt_instructions"], start=1
        )
    )

    prompt = f"""
{instructions}

Topic: {question["topic"]}
Difficulty: {question["difficulty"]}

Question: {question["question"]}

Answer:
"""

    payload = {
        "model": config["model_name"],
        "prompt": prompt,
        "stream": config["stream"],
        "options": {
            "temperature": config["temperature"],
            "num_predict": config["max_new_tokens"]
        }
    }

    start_time = time.perf_counter()

    response = requests.post(
        config["api_url"],
        json=payload,
        timeout=config["timeout"]
    )

    total_time = time.perf_counter() - start_time

    response.raise_for_status()
    result = response.json()

    answer = result["response"]
    generated_tokens = result.get("eval_count", 0)

    generation_time = (
        result.get("eval_duration", 0) / 1_000_000_000
    )

    tokens_per_second = (
        generated_tokens / generation_time
        if generation_time > 0
        else 0
    )

    return {
        "id": question["id"],
        "topic": question["topic"],
        "difficulty": question["difficulty"],
        "question": question["question"],
        "reference_answer": question["reference_answer"],
        "model_answer": answer,
        "total_time_seconds": round(total_time, 3),
        "generated_tokens": generated_tokens,
        "generation_time_seconds": round(generation_time, 3),
        "tokens_per_second": round(tokens_per_second, 2)
    }


def main():

    config = load_config()
    questions = load_questions()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    results = []

    print("Model:", config["model_name"])
    print("Prompt version:", config["prompt_version"])
    print("Maximum output tokens:", config["max_new_tokens"])
    print("Total evaluation questions:", len(questions))

    print("\nStarting optimized inference...\n")

    for index, question in enumerate(questions, start=1):

        print(
            f"[{index}/{len(questions)}] "
            f"Processing {question['id']} - {question['topic']}"
        )

        result = generate_answer(question, config)
        results.append(result)

        print("Generated tokens:", result["generated_tokens"])
        print("Response time:", result["total_time_seconds"], "seconds")
        print("Tokens per second:", result["tokens_per_second"])
        print()

    with OUTPUT_PATH.open("w", encoding="utf-8") as file:

        for result in results:
            file.write(
                json.dumps(result, ensure_ascii=False) + "\n"
            )

    print("Optimized inference completed!")
    print("Total answers generated:", len(results))
    print("Results saved to:", OUTPUT_PATH)


if __name__ == "__main__":
    main()
