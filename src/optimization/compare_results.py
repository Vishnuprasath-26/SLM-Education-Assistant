
import json
from pathlib import Path

BASELINE_PATH = Path("data/evaluation/baseline_metrics.json")
OPTIMIZED_PATH = Path("data/evaluation/optimized_metrics.json")
OUTPUT_PATH = Path("data/evaluation/optimization_comparison.json")


def load_json(path):
    with path.open("r", encoding="utf-8-sig") as file:
        return json.load(file)


def main():

    baseline = load_json(BASELINE_PATH)
    optimized = load_json(OPTIMIZED_PATH)

    baseline_time = baseline["average_response_time_seconds"]
    optimized_time = optimized["average_response_time_seconds"]

    baseline_speed = baseline["average_tokens_per_second"]
    optimized_speed = optimized["average_tokens_per_second"]

    time_improvement = (
        (baseline_time - optimized_time) / baseline_time
    ) * 100

    speed_improvement = (
        (optimized_speed - baseline_speed) / baseline_speed
    ) * 100

    comparison = {
        "baseline_response_time_seconds": baseline_time,
        "optimized_response_time_seconds": optimized_time,
        "response_time_improvement_percent": round(
            time_improvement, 2
        ),
        "baseline_tokens_per_second": baseline_speed,
        "optimized_tokens_per_second": optimized_speed,
        "generation_speed_improvement_percent": round(
            speed_improvement, 2
        ),
        "baseline_average_tokens": baseline["average_generated_tokens"],
        "optimized_average_tokens": optimized["average_generated_tokens"],
        "quality_evaluation_required": True
    }

    with OUTPUT_PATH.open("w", encoding="utf-8") as file:
        json.dump(comparison, file, indent=4)

    print("\nBASELINE VS OPTIMIZED")
    print("---------------------")

    for key, value in comparison.items():
        print(f"{key}: {value}")

    print("\nComparison saved to:", OUTPUT_PATH)


if __name__ == "__main__":
    main()
