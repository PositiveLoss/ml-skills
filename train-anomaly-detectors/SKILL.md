---
name: train-anomaly-detectors
description: "Train and assess novelty/anomaly detection models. Use for unlabeled/contaminated data, normal-only training, rare labels, drift, reconstruction scores and threshold calibration."
---

# Train anomaly detectors

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Define what counts as an anomaly, detection time and false-alert cost. Inspect label scarcity, delayed confirmation and contamination in nominal data.
2. Build entity/time-isolated evaluation and compare rule/statistical baselines. Separate outlier detection in a fixed dataset from novelty detection on future data.
3. Fit preprocessing and anomaly models on the permitted training population; choose thresholds from validation/operational false-alert budgets, not test labels.
4. Evaluate precision/recall, event-level latency and alerts per unit time under realistic prevalence. Check correlated repeated alerts and slice-specific false positives.
5. Monitor changing normal distributions, threshold behavior and feedback selection. Validate retraining/contamination policies with known injected and real anomalies.

## Acceptance evidence

Provide threshold protocol, base-rate-aware metrics and fixed alert budget. Avoid interpreting an uncalibrated anomaly score as a probability or claiming known-injection success covers all real anomalies.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
