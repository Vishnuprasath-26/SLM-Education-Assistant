
import json
from pathlib import Path
from statistics import mean

RESULTS_PATH = Path("data/evaluation/baseline_results.jsonl")
SCORES_PATH = Path("data/evaluation/baseline_scores.json")
OUTPUT_PATH = Path("data/evaluation/baseline_metrics.json")

QUALITY_CATEGORIES = [
    "correctness",
    "relevance",
    "completeness",
    "clarity"
]


def load_results():
    results = []

    with RESULTS_PATH.open("r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                results.append(json.loads(line))

    return results


def load_scores():
    with SCORES_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def calculate_metrics(results, scores):

    result_ids = {item["id"] for item in results}
    score_ids = {item["id"] for item in scores}

    if result_ids != score_ids:
        raise ValueError(
            "Evaluation result IDs and scoring IDs do not match."
        )

    if len(result_ids) != len(results) or len(score_ids) != len(scores):
        raise ValueError("Duplicate evaluation IDs found.")

    score_lookup = {
        item["id"]: item for item in scores
    }

    for score in scores:
        for category in QUALITY_CATEGORIES:
            value = score[category]

            if not isinstance(value, int) or value not in (0, 1, 2):
                raise ValueError(
                    f"Invalid {category} score for {score['id']}"
                )

    category_averages = {}

    for category in QUALITY_CATEGORIES:
        category_averages[category] = round(
            mean(score[category] for score in scores),
            2
        )

    total_quality_score = sum(
        sum(score[category] for category in QUALITY_CATEGORIES)
        for score in scores
    )

    maximum_quality_score = len(scores) * len(QUALITY_CATEGORIES) * 2

    quality_percentage = (
        total_quality_score / maximum_quality_score
    ) * 100

    average_response_time = mean(
        item["total_time_seconds"] for item in results
    )

    average_tokens_per_second = mean(
        item["tokens_per_second"] for item in results
    )

    average_generated_tokens = mean(
        item["generated_tokens"] for item in results
    )

    return {
        "model": "gemma3:1b",
        "total_questions": len(results),
        "quality_scores": category_averages,
        "total_quality_score": total_quality_score,
        "maximum_quality_score": maximum_quality_score,
        "quality_percentage": round(quality_percentage, 2),
        "average_response_time_seconds": round(
            average_response_time, 3
        ),
        "average_tokens_per_second": round(
            average_tokens_per_second, 2
        ),
        "average_generated_tokens": round(
            average_generated_tokens, 2
        )
    }


def main():

    results = load_results()
    scores = load_scores()

    metrics = calculate_metrics(results, scores)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_PATH.open("w", encoding="utf-8") as file:
        json.dump(metrics, file, indent=4)

    print("\n--- BASELINE EVALUATION METRICS ---")

    print("Model:", metrics["model"])
    print("Total questions:", metrics["total_questions"])

    print("\nQuality Scores:")

    for category, value in metrics["quality_scores"].items():
        print(f"{category.capitalize()}: {value}/2")

    print(
        "\nTotal quality score:",
        metrics["total_quality_score"],
        "/",
        metrics["maximum_quality_score"]
    )

    print("Quality percentage:", metrics["quality_percentage"], "%")

    print(
        "Average response time:",
        metrics["average_response_time_seconds"],
        "seconds"
    )

    print(
        "Average generation speed:",
        metrics["average_tokens_per_second"],
        "tokens/second"
    )

    print(
        "Average generated tokens:",
        metrics["average_generated_tokens"]
    )

    print("\nMetrics saved to:", OUTPUT_PATH)


if __name__ == "__main__":
    main()
