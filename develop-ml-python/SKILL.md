---
name: develop-ml-python
description: "Develop, review and test machine-learning integration in Python. Use for scikit-learn/PyTorch/JAX/TensorFlow orchestration and Python inference services, model/runtime compatibility, preprocessing parity, native resource ownership and reproducible inference/training boundaries."
---

# Python ML

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Inspect existing framework, environment and data contracts; use sklearn for appropriate tabular baselines and the established neural framework for existing models. Keep notebooks and reusable pipeline code aligned.
2. Implement fold-local preprocessing, explicit configs/seeds and clean train/eval boundaries. Verify shapes, finite values and versioned tokenizer/feature/label state.
3. Bound DataLoader/process/executor concurrency and capture dependencies/device versions. Keep blocking inference off async service loops and avoid unbounded background jobs.
4. Save model/preprocessor metadata and controlled checkpoints. Avoid loading untrusted pickle/custom model code; choose compatible persistence/export for the consumer.
5. Test clean imports, numerical fixtures, training/resume behavior and serving parity. Use project Ruff/type-check/test gates while preserving numerical assumptions.

## Acceptance evidence

Compile/test the actual language implementation with pinned dependencies. Compare golden input features and predictions against the training reference across supported shapes. Measure resource lifetime and end-to-end behavior; report unexecuted training/devices/backends explicitly.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
