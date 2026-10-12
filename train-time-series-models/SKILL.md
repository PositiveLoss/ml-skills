---
name: train-time-series-models
description: "Train and evaluate forecasting or temporal ML. Use for chronological backtesting, forecast horizons, covariates, overlapping windows, panel entities, seasonal baselines and time-dependent leakage."
---

# Train time-series models

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Define forecast origin/horizon, label availability, sampling interval and target entities. Distinguish future-known covariates from observed-only features.
2. Use rolling/expanding chronological backtests with appropriate gaps and entity constraints. Fit preprocessing within each origin's available data and avoid interpolation/backfills from the future.
3. Compare naive/seasonal baselines with candidate models under identical origins/horizons. Handle missing timestamps and changes in units/frequency deliberately.
4. Evaluate per-horizon/entity metrics and interval coverage; account for correlated overlapping errors and near-zero denominators. Tune using earlier validation windows.
5. Validate inference feature availability and retraining cadence. Stress test regime shifts, late arrivals and revised historical values.

## Acceptance evidence

Provide point-in-time feature evidence, chronological split checks and rolling baseline comparisons. Use block/entity-aware uncertainty and identify revisions/overlap in the evaluation.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
