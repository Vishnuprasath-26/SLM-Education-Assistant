
import json
from pathlib import Path
from statistics import mean

INPUT_PATH = Path("data/evaluation/optimized_results.jsonl")
OUTPUT_PATH = Path("data/evaluation/optimized_metrics.json")


def load_results():
    results = []

    with INPUT_PATH.open("r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                results.append(json.loads(line))

    return results


def calculate_metrics(results):

    response_times = [
        item["total_time_seconds"] for item in results
    ]

    generation_times = [
        item["generation_time_seconds"] for item in results
    ]

    generated_tokens = [
        item["generated_tokens"] for item in results
    ]

    token_speeds = [
        item["tokens_per_second"] for item in results
    ]

    total_tokens = sum(generated_tokens)
    total_generation_time = sum(generation_times)

    metrics = {
        "model_name": "gemma3:1b",
        "prompt_version": "optimized_v1",
        "total_questions": len(results),
        "average_response_time_seconds": round(
            mean(response_times), 3
        ),
        "minimum_response_time_seconds": round(
            min(response_times), 3
        ),
        "maximum_response_time_seconds": round(
            max(response_times), 3
        ),
        "average_generation_time_seconds": round(
            mean(generation_times), 3
        ),
        "average_generated_tokens": round(
            mean(generated_tokens), 2
        ),
        "total_generated_tokens": total_tokens,
        "average_tokens_per_second": round(
            mean(token_speeds), 2
        ),
        "overall_tokens_per_second": round(
            total_tokens / total_generation_time, 2
        ) if total_generation_time > 0 else 0
    }

    return metrics


def main():

    results = load_results()

    if not results:
        print("No optimized results found.")
        return

    metrics = calculate_metrics(results)

    with OUTPUT_PATH.open("w", encoding="utf-8") as file:
        json.dump(metrics, file, indent=4)

    print("\nOPTIMIZED MODEL PERFORMANCE")
    print("---------------------------")

    for key, value in metrics.items():
        print(f"{key}: {value}")

    print("\nMetrics saved to:", OUTPUT_PATH)


if __name__ == "__main__":
    main()
