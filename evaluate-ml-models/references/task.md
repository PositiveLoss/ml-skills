# Task reference

The bundled evaluator supports binary JSONL predictions (sample_id, y_true, probability, optional group_id), a fixed threshold, confusion metrics, Brier/log loss and a percentile bootstrap interval for accuracy. Undefined class-dependent metrics are null. It does not tune thresholds, calculate PR/ROC curves or prove calibration. Use task-specific tools for multiclass/ranking/regression/ASR. Read references/tools.md.

Primary sources:
- https://scikit-learn.org/stable/modules/model_evaluation.html
- https://scikit-learn.org/stable/modules/cross_validation.html
