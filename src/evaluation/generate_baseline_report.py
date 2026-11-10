
import json
from pathlib import Path

CONFIG_PATH = Path("configs/baseline_config.json")
METRICS_PATH = Path("data/evaluation/baseline_metrics.json")
OUTPUT_PATH = Path("reports/baseline_evaluation_report.md")


def load_json(path):
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def generate_report(config, metrics):

    quality_scores = metrics["quality_scores"]

    report = f"""# Baseline Model Evaluation Report

## 1. Project Overview

- Project: SLM Education Assistant
- Model: {metrics["model"]}
- Runtime: {config["runtime"]}
- Evaluation type: Baseline evaluation
- Total evaluation questions: {metrics["total_questions"]}

## 2. Model Configuration

| Configuration | Value |
|---|---|
| Model | {config["model_name"]} |
| Runtime | {config["runtime"]} |
| Temperature | {config["temperature"]} |
| Maximum output tokens | {config["max_new_tokens"]} |
| Streaming | {config["stream"]} |
| Timeout | {config["timeout"]} seconds |

## 3. Evaluation Metrics

### Quality Scores

| Metric | Average Score |
|---|---:|
| Correctness | {quality_scores["correctness"]}/2 |
| Relevance | {quality_scores["relevance"]}/2 |
| Completeness | {quality_scores["completeness"]}/2 |
| Clarity | {quality_scores["clarity"]}/2 |

### Overall Quality

- Total quality score: {metrics["total_quality_score"]}/{metrics["maximum_quality_score"]}
- Quality percentage: {metrics["quality_percentage"]}%

### Performance Metrics

| Metric | Result |
|---|---:|
| Average response time | {metrics["average_response_time_seconds"]} seconds |
| Average generation speed | {metrics["average_tokens_per_second"]} tokens/second |
| Average generated tokens | {metrics["average_generated_tokens"]} |

## 4. Observations

- The model generated answers for all evaluation questions.
- The average relevance score was {quality_scores["relevance"]}/2.
- Completeness received an average score of {quality_scores["completeness"]}/2.
- Some answers were incomplete or missed important details.
- Prompt instructions were introduced to encourage concise educational answers.
- The prompt-based experiment generated shorter answers than the earlier experiments that reached their configured token limits.

## 5. Limitations

- Evaluation was conducted using an initial set of only 10 questions.
- Quality scores were assigned manually using a 0-to-2 scoring rubric.
- Manual scoring can involve subjective judgment.
- The dataset currently contains only 22 records.
- The results may not represent performance across all educational topics and difficulty levels.
- No fine-tuning or model adaptation has been evaluated yet.
- The measured performance depends on the local hardware and runtime conditions.

## 6. Conclusion

Gemma 3 1B was evaluated as the baseline model for the SLM Education Assistant.

The model achieved an overall manual quality score of {metrics["quality_percentage"]}%.

Its average response time was {metrics["average_response_time_seconds"]} seconds, with an average generation speed of {metrics["average_tokens_per_second"]} tokens per second.

The evaluation identified completeness as an area requiring improvement.

These baseline results will be used as a reference for comparing future model adaptation and optimization experiments.

## 7. Output Files

- Configuration: configs/baseline_config.json
- Questions: data/evaluation/baseline_questions.jsonl
- Generated answers: data/evaluation/baseline_results.jsonl
- Manual scores: data/evaluation/baseline_scores.json
- Calculated metrics: data/evaluation/baseline_metrics.json
"""

    return report


def main():

    config = load_json(CONFIG_PATH)
    metrics = load_json(METRICS_PATH)

    report = generate_report(config, metrics)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    OUTPUT_PATH.write_text(report, encoding="utf-8")

    print("Baseline evaluation report generated successfully!")
    print("Model:", metrics["model"])
    print("Quality percentage:", metrics["quality_percentage"], "%")
    print("Report saved to:", OUTPUT_PATH)


if __name__ == "__main__":
    main()
