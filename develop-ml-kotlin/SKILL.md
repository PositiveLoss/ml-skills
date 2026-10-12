---
name: develop-ml-kotlin
description: "Develop, review and test machine-learning integration in Kotlin. Use for JVM inference and Android LiteRT/ONNX Runtime mobile integration, model/runtime compatibility, preprocessing parity, native resource ownership and reproducible inference/training boundaries."
---

# Kotlin ML

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Identify JVM server versus Android on-device execution; pin engine/runtime, native ABI and supported delegates/providers. Do not assume Kotlin provides a new native deep-learning backend.
2. Preserve preprocessing/tensor/label contracts and verify image/audio/text transformations. Check ByteBuffer dtype/order/capacity and model asset/version identity.
3. Own sessions/tensors through explicit lifecycle and keep inference off UI/Compose/audio realtime threads. Bound coroutine/executor work; cancellation must not free buffers still used by native calls.
4. Test app recreation/background, repeated inference, asset corruption and CPU fallback. Avoid rebuilding sessions during recomposition or sharing mutable input buffers between calls.
5. Compare predictions and sustained latency/memory/thermal behavior on actual supported devices. Keep training workflows distinct from validated mobile training capabilities.

## Acceptance evidence

Compile/test the actual language implementation with pinned dependencies. Compare golden input features and predictions against the training reference across supported shapes. Measure resource lifetime and end-to-end behavior; report unexecuted training/devices/backends explicitly.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
