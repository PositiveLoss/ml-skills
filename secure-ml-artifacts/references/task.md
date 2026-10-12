# Task reference

Weights-only/safetensors-style storage can reduce executable deserialization risks but does not certify all runtime behavior or eliminate resource exhaustion. ONNX custom ops and parsers still require versioned dependencies. trust_remote_code is an execution decision, not a harmless model option. Avoid including secrets and raw sensitive records in reproducibility bundles.

Primary sources:
- https://scikit-learn.org/stable/model_persistence.html
- https://huggingface.co/docs/safetensors/index
- https://docs.pytorch.org/docs/stable/notes/serialization.html
