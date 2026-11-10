
# Model Adaptation Feasibility Report

## 1\. Project Model

Selected model: gemma3:1b
Runtime: Ollama
Adaptation methods investigated: Full Fine-Tuning, LoRA, QLoRA

## 2\. Hardware Environment

* Python: 3.12.10
* Total RAM: 7.68 GB
* Available RAM during assessment: 1.56 GB
* Processor: Intel Core i3-1215U
* Graphics: Intel UHD integrated graphics
* CUDA: Not available
* PyTorch: 2.15.0+cpu

## 3\. Installed Training Libraries

* Transformers: 5.22.1
* PEFT: 0.21.2
* bitsandbytes: Not installed

## 4\. Feasibility Assessment

### Full Fine-Tuning

Not attempted because the available system memory is insufficient
for a practical training experiment with the selected model.

### LoRA

PEFT is installed, but only 1.56 GB RAM was available during
the assessment. CPU-based training is therefore not considered
practical on the current machine.

### QLoRA

Not attempted because CUDA is unavailable and bitsandbytes
is not installed. Compatibility has not been established.

## 5\. Decision

Model fine-tuning will not be attempted on the current local
machine because of hardware and memory limitations.

A suitable machine or cloud GPU environment may be considered
for a future LoRA or QLoRA experiment.

## 6\. Important Dataset Limitation

The current educational dataset contains only 22 records.
It must be expanded and validated before a meaningful
fine-tuning experiment can be conducted.

## 7\. Conclusion

The adaptation environment was assessed, but no fine-tuning
was performed. The decision not to train locally is based on
the available hardware, memory and package configuration.
