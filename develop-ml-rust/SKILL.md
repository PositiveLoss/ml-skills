---
name: develop-ml-rust
description: "Develop, review and test machine-learning integration in Rust. Use for native Burn training or established ort/other runtime inference, model/runtime compatibility, preprocessing parity, native resource ownership and reproducible inference/training boundaries."
---

# Rust ML

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Choose training versus inference explicitly. Inspect Burn/backend support for native training or the pinned Rust binding such as ort for ONNX inference; do not equate model loading with autograd training support.
2. Match runtime native libraries, execution provider, target architecture and tensor dtype/shape. Preserve preprocessing and output maps from the training producer.
3. Use ownership/RAII for sessions, device buffers and streams; validate borrowing/lifetimes around FFI and avoid holding locks across asynchronous waits.
4. Bound CPU/native threading and inference queues; isolate blocking kernels from Tokio workers with explicit cancellation/cleanup semantics. Verify claimed zero-copy behavior rather than guessing from slice APIs.
5. Test numerical/golden parity, invalid shapes, repeated load/run/drop and packaging on supported targets. If training, verify gradients, checkpoints and optimizer state on the actual backend.

## Acceptance evidence

Compile/test the actual language implementation with pinned dependencies. Compare golden input features and predictions against the training reference across supported shapes. Measure resource lifetime and end-to-end behavior; report unexecuted training/devices/backends explicitly.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
