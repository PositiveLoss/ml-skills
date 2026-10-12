# Task reference

The hash helper creates/verifies a JSON manifest for files inside a declared root, rejects path escape and reports missing or modified files. It records integrity rather than provenance/authenticity and cannot ensure dataset permissions or reproducible execution. Read references/tools.md. RNG seed identity alone does not guarantee identical CPU/GPU or framework-version results.

Primary sources:
- https://docs.pytorch.org/docs/stable/notes/randomness.html
- https://docs.pytorch.org/docs/stable/notes/serialization.html
