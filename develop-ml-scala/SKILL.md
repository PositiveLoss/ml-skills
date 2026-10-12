---
name: develop-ml-scala
description: "Develop, review and test machine-learning integration in Scala. Use for Spark ML pipelines and JVM native runtime inference, model/runtime compatibility, preprocessing parity, native resource ownership and reproducible inference/training boundaries."
---

# Scala ML

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Choose distributed tabular training with Spark ML versus JVM runtime inference. Pin Scala/Spark binary versions, engine and native libraries; distinguish driver and executor resource ownership.
2. Keep feature transformers/estimators in fold-correct pipelines with immutable dataset/split identity. Enforce entity/time splits before Spark transformations and joins.
3. Control repartitioning, cached datasets and random seeds; verify label/feature/vector column metadata and evaluator aggregation. Avoid collecting large predictions to the driver.
4. For native inference, initialize sessions per justified executor/partition scope, close tensors/results and bound concurrency. Test serialization assumptions instead of shipping nonserializable sessions in closures.
5. Run JVM/Spark integration tests, small known numerical fixtures and model/preprocessor save/reload parity. Measure executor-native memory and skew, not just driver heap.

## Acceptance evidence

Compile/test the actual language implementation with pinned dependencies. Compare golden input features and predictions against the training reference across supported shapes. Measure resource lifetime and end-to-end behavior; report unexecuted training/devices/backends explicitly.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
