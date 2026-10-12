---
name: design-ml-data-splits
description: "Design leakage-resistant ML evaluation splits. Use for speaker/user/group splits, temporal validation, nested cross-validation, duplicate families, calibration holdouts and train/test contamination."
---

# Design ML data splits

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Define independent units and the intended generalization claim: new user, site, speaker, recording session, future period or known entity. Select group/time/spatial boundaries accordingly.
2. Construct split membership before learned preprocessing or augmentation. Keep all crops/windows/segments/near duplicates of a source within its allowed group.
3. Use chronological splits with gaps/embargo when features/targets overlap future windows. Never shuffle future outcomes into training to improve class balance.
4. Reserve tuning/calibration data and a blind final holdout. Use nested CV when estimating a tuned procedure; perform imputation, scaling, resampling and selection independently within training folds.
5. Persist sample IDs and split rules, then verify group/content overlap and time boundaries with negative fixtures. Explain unavoidable distribution shifts and sparse class/group combinations.

## Acceptance evidence

Provide immutable split manifests, split-population summaries and executable overlap checks. Demonstrate that adding a segment from a held-out speaker/session is detected; mark temporal checks separately from hash checks.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
