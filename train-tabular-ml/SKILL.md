---
name: train-tabular-ml
description: "Train and diagnose tabular classification/regression models with leakage-safe pipelines. Use for linear/tree/boosting baselines, missing or categorical features, imbalance, cross-validation and structured-data model comparison."
---

# Train tabular ML

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

Read [executable helper](references/tools.md) before using the bundled script and fixtures.

## Workflow

1. Establish the target, groups/time split and dummy/simple baseline. Inspect sample count, label frequency, categorical cardinality and missingness before selecting an estimator.
2. Build fold-local preprocessing and fit logistic/linear or small tree ensembles first. Compare more complex models under identical folds, features, tuning budgets and metric definitions.
3. Handle class imbalance via cost/metric/threshold design; if resampling is used, apply it only inside training folds. Avoid treating accuracy or ROC-AUC alone as rare-event utility.
4. Inspect learning curves, error slices, calibration and feature dependence. Use validation for hyperparameters/decision thresholds and preserve a blind final test.
5. Save feature/schema/label metadata and a reproducible report; verify clean-runtime inference and model artifact trust requirements.

## Acceptance evidence

Run the bundled offline sklearn baseline, compare its validation score with a DummyClassifier, and confirm scaling statistics use only train indices. Report folds, test sample count and baseline/candidate results without extrapolating toy-data quality.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
