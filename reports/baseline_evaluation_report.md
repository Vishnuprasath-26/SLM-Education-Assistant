# Baseline Model Evaluation Report

## 1. Project Overview

- Project: SLM Education Assistant
- Model: gemma3:1b
- Runtime: ollama
- Evaluation type: Baseline evaluation
- Total evaluation questions: 10

## 2. Model Configuration

| Configuration | Value |
|---|---|
| Model | gemma3:1b |
| Runtime | ollama |
| Temperature | 0 |
| Maximum output tokens | 350 |
| Streaming | False |
| Timeout | 180 seconds |

## 3. Evaluation Metrics

### Quality Scores

| Metric | Average Score |
|---|---:|
| Correctness | 1.6/2 |
| Relevance | 2/2 |
| Completeness | 1.3/2 |
| Clarity | 1.6/2 |

### Overall Quality

- Total quality score: 65/80
- Quality percentage: 81.25%

### Performance Metrics

| Metric | Result |
|---|---:|
| Average response time | 14.342 seconds |
| Average generation speed | 18.09 tokens/second |
| Average generated tokens | 169.5 |

## 4. Observations

- The model generated responses for all 10 evaluation questions.
- The average manual quality score was 81.25%.
- Relevance achieved an average score of 2/2.
- Completeness achieved an average score of 1.3/2, indicating that some answers missed important details.
- E001, E003, E004 and E007 were identified as incomplete or requiring improvement.
- Prompt engineering reduced the generated response lengths compared with the earlier experiments that reached the configured token limits.

## 5. Limitations

- The evaluation used only 10 questions.
- The current educational dataset contains only 22 records.
- Quality scores were assigned manually and may involve subjective judgment.
- Some generated answers were incomplete.
- Model performance depends on local hardware and runtime conditions.
- Fine-tuning and model optimization have not yet been evaluated.
- The evaluation does not cover all possible educational questions or difficulty levels.

## 6. Conclusion

Gemma 3 1B was evaluated as the baseline model for the SLM Education Assistant.

The model achieved an overall manual quality score of 81.25%.

Its average response time was 14.342 seconds, with an average generation speed of 18.09 tokens per second.

The evaluation identified completeness as an area requiring improvement.

These baseline results will be used as a reference for comparing future model adaptation and optimization experiments.

## 7. Output Files

- Configuration: configs/baseline_config.json
- Questions: data/evaluation/baseline_questions.jsonl
- Generated answers: data/evaluation/baseline_results.jsonl
- Manual scores: data/evaluation/baseline_scores.json
- Calculated metrics: data/evaluation/baseline_metrics.json
