---
name: train-ml-with-tensorflow
description: "Implement TensorFlow/Keras ML training and deployment boundaries. Use for tf.data, custom train_step, losses, masking, mixed precision, tf.function retracing, checkpoints and export signatures."
---

# Train ML with TensorFlow

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Pin compatible TensorFlow/Keras versions and choose built-in fit or custom training only as needed. Inspect dtype policy, devices and dataset cardinality/shapes.
2. Check one eager forward/backward step, losses, trainable variables and masks. Keep target encodings compatible with logits/probabilities and the chosen loss.
3. Build deterministic, bounded tf.data pipelines where needed; separate train-only augmentations from eval preprocessing and control cache/shuffle placement.
4. Limit retracing with deliberate shapes/signatures and verify tf.function behavior against eager results. Apply mixed precision and distributed loss normalization using supported APIs.
5. Test resumable optimizer/checkpoint state and exported signature inputs/outputs with the target runtime. Account for Keras-version differences in save/export formats.

## Acceptance evidence

Provide eager-vs-graph parity, tiny-batch learning, train/eval masking checks and a restored-model prediction test. State whether TensorFlow, accelerator and distributed checks were actually available.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
