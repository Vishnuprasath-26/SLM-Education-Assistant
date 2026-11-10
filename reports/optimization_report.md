# M6 – Model Optimization Experiment Report

## 1. Objective

The objective of this experiment was to improve the inference performance of the Gemma 3 1B model while maintaining or improving answer quality.

## 2. Base Model and Runtime

- Model: Gemma 3 1B
- Runtime: Ollama
- API: Ollama Generate API
- Temperature: 0
- Evaluation questions: 10

## 3. Optimization Techniques

The following optimization techniques were applied:

1. Prompt optimization: Updated the instructions to generate concise, direct answers in simple English.
2. Output token reduction: Reduced the maximum output token limit from 350 to 220.
3. Response control: Added instructions to include essential technical points and avoid unnecessary repetition.

Note: Both prompt instructions and token limit were changed together. Therefore, the experiment measures their combined effect.

## 4. Baseline Performance

| Metric | Baseline |
|---|---:|
| Average response time | 14.342 seconds |
| Average generation speed | 18.09 tokens/second |
| Average generated tokens | 169.5 |
| Quality score | 81.25% |

## 5. Optimized Performance

| Metric | Optimized |
|---|---:|
| Average response time | 10.210 seconds |
| Average generation speed | 19.53 tokens/second |
| Average generated tokens | 119.9 |
| Quality score | 90% |

## 6. Performance Comparison

- Response time reduction: 28.81%.
- Generation speed improvement: 7.96%.
- Quality score improvement: 8.75 percentage points.
- Average generated tokens reduced from 169.5 to 119.9.

## 7. Quality Evaluation

Ten evaluation questions were manually scored using four criteria:

- Correctness
- Relevance
- Completeness
- Clarity

Each criterion was scored from 0 to 2.

Baseline score: 65/80 (81.25%).

Optimized score: 72/80 (90%).

The optimized answers achieved a higher preliminary manual quality score. However, some weaknesses remained, including an incomplete response for E003 and a technical explanation issue in E006.

## 8. Limitations

- Evaluation was conducted using only 10 questions.
- Quality scoring was manual and subjective.
- Prompt instructions and token limit were changed simultaneously.
- Inference timing can vary depending on system load and runtime conditions.
- The optimized responses still require further review for factual accuracy and completeness.
- No model weights were changed or fine-tuned during this optimization experiment.

## 9. Conclusion

The combined prompt and output-token optimization experiment improved the measured inference performance of Gemma 3 1B.

Average response time decreased by 28.81%, generation speed increased by 7.96%, and the preliminary manual quality score improved from 81.25% to 90%.

The experiment demonstrates that inference optimization through prompt engineering and output control can improve the measured performance without modifying the underlying model weights.

Further evaluation using a larger held-out dataset and repeated benchmark runs is recommended.
