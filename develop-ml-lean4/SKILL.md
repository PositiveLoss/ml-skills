---
name: develop-ml-lean4
description: "Develop, review and test machine-learning integration in Lean 4. Use for formal ML invariants and bounded native/service inference bridges, model/runtime compatibility, preprocessing parity, native resource ownership and reproducible inference/training boundaries."
---

# Lean 4 ML

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Specify which property is proved: dimensions, bounded conversions, algorithm invariants or error bounds. Separate pure mathematical models from runtime library/weights/hardware assumptions.
2. Implement checked input/output conversions and a narrow IO boundary to a verified native/service runtime. Do not claim a general native Lean training backend or convert untrusted predictions into axioms.
3. For FFI honor the pinned Lean ABI, object ownership/borrowing, module/thread initialization and external-object finalizers. For IPC define bounded framing, model identity, deadlines and errors.
4. Prove pure invariants without sorry, and test the actual bridge/encoding/finite-value/range checks separately. Include floating-point semantics or clearly stated abstraction assumptions.
5. Run lake build and executable golden-inference tests plus native sanitizers where needed. Report what the proof covers and which empirical generalization claims remain unproved.

## Acceptance evidence

Compile/test the actual language implementation with pinned dependencies. Compare golden input features and predictions against the training reference across supported shapes. Measure resource lifetime and end-to-end behavior; report unexecuted training/devices/backends explicitly.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
