---
name: adapt-foundation-models
description: "Adapt pretrained/foundation models with full fine-tuning, LoRA/PEFT or task heads. Use for SFT data formatting, frozen parameters, adapter/base compatibility, quantized training, retention and evaluation contamination."
---

# Adapt foundation models

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Define the downstream task, base model/tokenizer revision, data permissions and serving constraints. Establish frozen/prompted/task-head baselines before fine-tuning.
2. Split by original source/entity/time and inspect prompt/response/evaluation overlap. Verify labels, loss masks, chat template/special tokens and packing boundaries.
3. Choose trainable components and confirm actual gradients/parameter counts. Pin PEFT/quantization/backend compatibility and budget memory before enabling mixed/low precision.
4. Compare training loss with held-out task quality, retention/catastrophic forgetting and relevant multilingual/robustness slices. Keep tuning and final evaluation independent.
5. Save adapter plus exact base/tokenizer/preprocessing identity; test merge/non-merge and exported serving outputs. Document unsupported merge/quantization paths rather than patching generated weights blindly.

## Acceptance evidence

Provide a trainable-parameter check, tiny SFT alignment example, held-out benchmark and adapter restoration test. Distinguish better task behavior from memorization or leakage.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
