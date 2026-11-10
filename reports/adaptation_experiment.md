
# LoRA Adaptation Experiment

## 1. Objective

Investigate adapting Gemma 3 1B for educational question answering
using Low-Rank Adaptation (LoRA).

## 2. Base Model

Model: google/gemma-3-1b-it

## 3. Proposed Adaptation Method

LoRA (Low-Rank Adaptation).

The original model weights would remain frozen while additional
low-rank adapter weights would be trained.

## 4. Proposed Configuration

- LoRA rank: 8
- LoRA alpha: 16
- LoRA dropout: 0.05
- Learning rate: 0.0002
- Epochs: 3
- Batch size: 1
- Gradient accumulation: 8
- Maximum sequence length: 512

Refer to configs/adaptation_config.json for the complete configuration.

## 5. Dataset

- Training: 15 records
- Validation: 3 records
- Testing: 4 records

Dataset format: Conversational JSONL (SFT).

## 6. Hardware

- Total RAM: 7.68 GB
- Available RAM during assessment: 1.56 GB
- CPU: Intel Core i3-1215U
- GPU: Intel UHD integrated graphics
- CUDA: Not available

## 7. Experiment Status

Status: NOT EXECUTED.

Reason:
The available system memory and CPU-only environment are
not considered sufficient for a practical local training experiment.

## 8. Limitations

- Dataset contains only 22 records.
- Training data contains only 15 records.
- No adapter weights were generated.
- No training loss or validation loss was measured.
- No fine-tuned model was produced.

## 9. Future Work

- Expand and validate the educational dataset.
- Verify LoRA target modules against the model architecture.
- Use a suitable GPU-enabled environment.
- Run training and record actual training metrics.
- Compare the adapted model against the baseline model.

## 10. Conclusion

LoRA was selected as the proposed adaptation method.
The configuration and experiment plan were documented,
but training was not executed because of hardware limitations.
