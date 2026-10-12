---
name: develop-ml-java
description: "Develop, review and test machine-learning integration in Java. Use for ONNX Runtime Java, DJL or established JVM training/inference, model/runtime compatibility, preprocessing parity, native resource ownership and reproducible inference/training boundaries."
---

# Java ML

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Inspect ONNX Runtime/DJL/other chosen engine and compatible JVM/native packages. Distinguish engine-supported training from inference-only integration.
2. Version tensor names/shapes/dtypes and preprocess/tokenizer/label state. Verify direct buffers, numeric casting and batch layout against the training reference.
3. Scope sessions, tensors and native result objects with documented close/manager ownership. Reuse sessions safely, bound executor and native thread pools, and avoid per-request model loading.
4. Handle inference timeout/cancellation and engine failure explicitly; test whether native operations can be interrupted. Preserve model version identity through the service.
5. Run JUnit/build checks, golden parity, repeated resource lifecycle and target-OS packaging. For training, test gradients/checkpoints through the selected engine API.

## Acceptance evidence

Compile/test the actual language implementation with pinned dependencies. Compare golden input features and predictions against the training reference across supported shapes. Measure resource lifetime and end-to-end behavior; report unexecuted training/devices/backends explicitly.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
