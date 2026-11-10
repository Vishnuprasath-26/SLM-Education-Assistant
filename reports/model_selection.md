# SLM Model Selection and Baseline Evaluation

## 1. Selected Model

**Model Name:** Gemma 3 1B Instruct
**Provider:** Google
**Model Runtime:** Ollama
**Model Tag:** gemma3:1b
**Quantization:** Q4_K_M
**Model Size:** Approximately 806 MB

## 2. Reason for Selection

Gemma 3 1B was selected for the Education Assistant project because it is a lightweight language model that can run locally using Ollama.

Our development laptop has 8 GB RAM, an Intel i3-1215U processor and integrated graphics. Therefore, a smaller model is more suitable for our initial experiments than larger language models.

## 3. Initial Testing

The model was tested with educational questions about:

- Artificial Intelligence
- Machine Learning
- Python variables and data types

The model generated structured explanations with headings, definitions and real-life examples.

## 4. Baseline Performance

| Metric | Result |
|---|---:|
| Total response time | 17.32 seconds |
| Generation time | 13.08 seconds |
| Generated tokens | 150 |
| Tokens per second | 11.47 |

## 5. Initial Observations

- The model successfully generated educational explanations.
- Answers were organized and beginner-friendly.
- The model provided relevant real-life examples.
- Some answers contained unnecessary follow-up questions.
- The response was truncated because the output limit was set to 150 tokens.

## 6. Limitations

The model may occasionally produce inaccurate information or incomplete answers. Further evaluation is required using a dedicated test dataset.

## 7. Conclusion

Gemma 3 1B is selected as the initial SLM for the Education Assistant. Its response quality and CPU inference performance will be evaluated further before applying model optimization or adaptation.
