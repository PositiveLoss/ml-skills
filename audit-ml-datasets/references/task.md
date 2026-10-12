# Task reference

Use scripts/audit_manifest.py for exact ID, group and SHA-256 overlap checks on JSONL. Required fields: sample_id, split (train/validation/test), group_id and content_sha256. The helper validates metadata only; it does not calculate file hashes, inspect consent, detect near duplicates or establish chronological validity. Read references/tools.md before running it.

Primary sources:
- https://scikit-learn.org/stable/common_pitfalls.html
- https://huggingface.co/docs/datasets/about_dataset_features
