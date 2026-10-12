---
name: develop-ml-cpp
description: "Develop, review and test machine-learning integration in C++. Use for ONNX Runtime C++/LibTorch inference and supported native training, model/runtime compatibility, preprocessing parity, native resource ownership and reproducible inference/training boundaries."
---

# C++ ML

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Inspect runtime/format/API version and choose ONNX Runtime or compatible LibTorch/native engine. Match compiler/stdlib/ABI/CUDA/provider packages instead of assuming Python wheel compatibility.
2. Validate tensor dtype, shape, strides, device and preprocessing against producer golden inputs. Distinguish borrowed/from-blob buffers from owning tensors and test lifetime/copy semantics.
3. Use RAII for sessions/options/results and explicit thread/device/stream ownership. Bound inference queues and native pools; avoid blocking callbacks/realtime threads.
4. For native training verify autograd, train/eval modes, optimizer/checkpoint state and loss reduction. For inference verify the model format/export route supported by the installed runtime.
5. Run CMake/CTest and applicable sanitizers, repeated lifecycle and numerical/runtime parity. Measure device-synchronized latency and actual native memory.

## Acceptance evidence

Compile/test the actual language implementation with pinned dependencies. Compare golden input features and predictions against the training reference across supported shapes. Measure resource lifetime and end-to-end behavior; report unexecuted training/devices/backends explicitly.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
