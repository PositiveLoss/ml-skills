---
name: export-ml-models
description: "Export ML models to ONNX or target deployment formats and verify parity. Use for opset/IR/runtime compatibility, dynamic shapes, preprocess/tokenizer metadata, unsupported operators and multi-language inference."
---

# Export ML models

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

Read [executable helper](references/tools.md) before using the bundled script and fixtures.

## Workflow

1. Inspect source model mode, preprocessing, supported shape/dtype range and target runtime/provider versions. Choose export API and format supported by the installed framework.
2. Export model plus input/output, tokenizer/label and normalization contracts. Pin opset/IR and external weight files where relevant; avoid implying dynamic shapes from a single traced example.
3. Validate the graph, load it with the actual target runtime and inspect unsupported/custom operators and provider fallback. Test batch/shape boundaries.
4. Compare source/target predictions numerically and on task metrics with fixed golden inputs. Use dtype-appropriate absolute/relative tolerances and investigate decision changes.
5. Package artifact hashes and version requirements, then run inference from the consuming language/platform. Mark unexecuted consumers explicitly.

## Acceptance evidence

Run scripts/compare_arrays.py on equal, tolerated and intentionally mismatched tensors; verify shape/NaN/empty inputs fail. Add real source-vs-export target-runtime tests for the model being exported.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
