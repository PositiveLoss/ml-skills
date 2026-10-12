---
name: monitor-ml-models
description: "Monitor deployed ML input, prediction and quality behavior. Use for data/concept drift, delayed labels, calibration changes, slice metrics, alert thresholds, model rollout comparisons and retraining signals."
---

# Monitor ML models

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Define model/data identity, monitored population, latency/failure metrics and independent outcome labels. Separate service health from model-quality monitoring.
2. Track input/missingness/feature distribution and output/calibration/coverage slices with bounded aggregation and approved retention. Identify delayed or selectively observed labels.
3. Compare deployed cohorts/versions using matched evaluation windows and traffic policy. Evaluate drift measures against baseline variability and multiple testing.
4. Set actionable alert thresholds, minimum sample sizes, ownership and investigation steps. Treat detected distribution shift as a signal, not proof that quality deteriorated.
5. Design shadow/canary rollback and retraining criteria, then test synthetic schema/shift/failure incidents. Preserve label feedback without contaminating future evaluation.

## Acceptance evidence

Provide monitor definitions, label-delay/selection assumptions, example incident response and false-alarm checks. Demonstrate that a healthy server with poor quality and a shifted but still accurate model are distinguished.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
