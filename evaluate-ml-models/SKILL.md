---
name: evaluate-ml-models
description: "Evaluate ML models with decision-appropriate metrics and uncertainty. Use for held-out benchmarks, confusion matrices, imbalance, threshold comparisons, grouped bootstrap, quality slices and paired candidate/baseline testing."
---

# Evaluate ML models

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

Read [executable helper](references/tools.md) before using the bundled script and fixtures.

## Workflow

1. Freeze the dataset, model and threshold policy before final evaluation. Join every prediction ID to the frozen split/label manifest and check label/group identity. Record sample population, independent units, labels, missing/abstained predictions and metric definitions.
2. Compute task metrics and denominators, including failure/coverage rates. Choose PR-oriented metrics for relevant rare events and calibrated probability scores when probabilities matter.
3. Evaluate subgroup/domain/time slices and paired baseline/candidate outputs. Resample users/speakers/sessions rather than correlated rows; use time blocks for temporal dependence. Check interval stability as bootstrap draws increase and report too few independent units explicitly.
4. Keep threshold selection/calibration on validation data. State class-absent/undefined metrics and interval assumptions instead of manufacturing zeros or confidence.
5. Report uncertainty, repeated-selection effects and resource tradeoffs. Do not convert a toy/synthetic score into a real-world quality claim.

## Acceptance evidence

Run scripts/evaluate_predictions.py on known confusion-matrix and imbalanced fixtures; verify invalid labels/probabilities/duplicate IDs fail. Compare outputs against sklearn metrics and verify seeded grouped bootstrap repeatability.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
