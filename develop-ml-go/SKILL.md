---
name: develop-ml-go
description: "Develop, review and test machine-learning integration in Go. Use for Gonum numerical models, maintained Go bindings or model-service clients, model/runtime compatibility, preprocessing parity, native resource ownership and reproducible inference/training boundaries."
---

# Go ML

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Decide between numerical/statistical training, local runtime inference and a remote service. Inspect a maintained project-selected Go binding and its native compatibility; do not invent an official ONNX Go SDK.
2. Specify input/output feature order, dtype, shape and preprocessing from the producer model. Verify slices, tensor buffer lifetime and native allocation/free behavior at the binding boundary.
3. Reuse validated sessions/clients, bound worker queues and account for native threads/cgo overhead. Context cancellation may stop waiting without interrupting a native kernel; document it.
4. Keep numerical training logic testable with small known problems, explicit RNG and group/time-correct splits. Avoid assuming Gonum alone supplies a full deep-learning stack.
5. Run go test/race where applicable, golden prediction parity and repeated session teardown. Test deployment native libraries and cross-platform build constraints.

## Acceptance evidence

Compile/test the actual language implementation with pinned dependencies. Compare golden input features and predictions against the training reference across supported shapes. Measure resource lifetime and end-to-end behavior; report unexecuted training/devices/backends explicitly.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
