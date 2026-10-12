---
name: secure-ml-artifacts
description: "Audit ML artifact and data handling security. Use for unsafe model deserialization, remote custom code, hash/provenance checks, training-data privacy, poisoning/supply-chain exposure and inference abuse limits."
---

# Secure ML artifacts

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Identify artifact/data suppliers, trust boundaries and execution paths. Inspect loading formats, remote/custom code and dependency/runtime libraries actually reachable in the project.
2. Verify artifact origin/version and integrity before loading. Avoid arbitrary pickle/joblib/custom deserialization from untrusted sources; evaluate safe formats and constrained runtimes appropriate to the model.
3. Isolate untrusted parsers/models with bounded memory/CPU/file/network permissions where needed. Review custom operators, external-data paths and model loading side effects.
4. Minimize sensitive examples/metadata in tracking, logs and exported assets. Confirm dataset use/licensing rules from actual sources and protect feedback/annotation channels against poisoning.
5. Add tests for tampered/missing artifacts, path escape, malformed huge inputs and unauthorized loading. Report evidenced reachable findings rather than blanket speculative risks.

## Acceptance evidence

Provide a trust/format inventory and executed rejection tests. Hash equality must be described as integrity, not origin/authenticity; use signatures or trusted manifests when provenance matters.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
