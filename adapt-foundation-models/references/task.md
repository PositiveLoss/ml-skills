# Task reference

LoRA adapters are not self-contained replacements for base weights. Quantized loading, adapter training and adapter merging have different compatibility requirements. Instruction fine-tuning should mask tokens according to the intended objective rather than defaulting to all input tokens. Do not treat lower perplexity as proof of improved factual accuracy or tool use.

Primary sources:
- https://huggingface.co/docs/peft/index
- https://huggingface.co/docs/trl/sft_trainer
- https://huggingface.co/docs/transformers/main_classes/quantization
