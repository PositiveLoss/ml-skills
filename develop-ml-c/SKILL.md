---
name: develop-ml-c
description: "Develop, review and test machine-learning integration in C. Use for ONNX Runtime C API and explicit native training/bridge boundaries, model/runtime compatibility, preprocessing parity, native resource ownership and reproducible inference/training boundaries."
---

# C ML

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Select actual inference/training capabilities of the chosen native library. Prefer ONNX Runtime C API for compatible inference; keep unsupported training behind a defined bridge rather than inventing high-level C training APIs.
2. Define tensor dimensions/dtypes, feature order, buffer size/alignment and preprocessing. Check overflow when calculating element/byte counts and reject invalid/mismatched inputs.
3. Specify ownership and cleanup for environment/session/options/tensors/results/status objects. Preserve input buffers for documented run duration and avoid crossing allocators with mismatched frees.
4. Bound native thread pools and concurrent calls. Handle errors/cancellation/model reload without freeing in-flight resources; test target library/API version negotiation.
5. Compile a C-only consumer, run sanitizers and golden prediction parity, and verify repeated load/run/free and platform packaging.

## Acceptance evidence

Compile/test the actual language implementation with pinned dependencies. Compare golden input features and predictions against the training reference across supported shapes. Measure resource lifetime and end-to-end behavior; report unexecuted training/devices/backends explicitly.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
