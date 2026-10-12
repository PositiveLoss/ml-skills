---
name: train-text-models
description: "Train and evaluate text ML/NLP including classification, extraction and retrieval encoders. Use for tokenizer versions, document/source leakage, truncation, multilingual/code-switch text and task-specific decoding."
---

# Train text models

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Define labels/spans/retrieval targets and deployment languages/documents. Inspect duplicate templates, authors, source domains and pretrained/evaluation overlap.
2. Split original documents/entities/time before chunks or paraphrases. Construct negatives from training data under the declared retrieval/task protocol.
3. Pin tokenizer/vocabulary/special tokens and preprocessing. Verify Unicode, truncation, sequence labels, offsets, padding masks and target alignment.
4. Compare bag-of-words/linear or frozen-encoder baselines with fine-tuned models under equivalent splits/budgets. Check tiny examples and evaluate long/short/multilingual slices.
5. Report task metrics and fixed decoding/threshold policy; package tokenizer/label mappings with the model and test consumer parity.

## Acceptance evidence

Provide tokenizer/offset fixtures, source-isolated evaluation and baseline/candidate results. Report coverage lost through truncation and unknown languages rather than ignoring dropped content.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
