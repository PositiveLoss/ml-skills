---
name: calibrate-ml-predictions
description: "Calibrate classification probabilities and decision thresholds honestly. Use for reliability diagrams, sigmoid/isotonic/temperature scaling, ECE/Brier/log loss, abstention and distribution-shift checks."
---

# Calibrate ML predictions

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Identify whether the output is a probability, score or logit, and what decision consumes it. Freeze the base model and reserve independent calibration data.
2. Compare reliability curves, probability distribution and proper scoring rules; interpret Brier/log loss as combining more than calibration alone.
3. Fit the selected calibrator only on out-of-training predictions. Choose method complexity according to calibration-set size and preserve class support.
4. Tune operational thresholds on validation/calibration units from error cost/coverage constraints. Keep the final test separate from both calibrator fitting and threshold selection.
5. Evaluate calibration, discrimination and selective coverage across deployment slices/time. Define recalibration policy under shift without assuming calibration transfers unchanged.

## Acceptance evidence

Provide untouched evaluation reliability bins/counts, scoring-rule comparison and fixed threshold/coverage results. Test missing classes, extreme logits and changed class priors.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
