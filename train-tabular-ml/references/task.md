# Task reference

scripts/train_baseline.py uses local sklearn breast-cancer toy data, a deterministic train/validation/test split and StandardScaler/LogisticRegression Pipeline. It exports metrics and split identities as JSON, not an unsafe pickle. It is a small reproducibility fixture, not a production dataset benchmark. Read references/tools.md for arguments and dependency versions.

Primary sources:
- https://scikit-learn.org/stable/modules/linear_model.html
- https://scikit-learn.org/stable/modules/ensemble.html
- https://scikit-learn.org/stable/common_pitfalls.html
