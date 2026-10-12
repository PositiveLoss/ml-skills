---
name: design-active-learning
description: "Design and evaluate active learning or annotation acquisition loops. Use for uncertainty/diversity sampling, label budgets, annotator disagreement, pool bias and iterative dataset updates."
---

# Design active learning

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Define annotation unit, cost, pool, oracle/annotator behavior and fixed blind evaluation. Identify related sources that must remain grouped across acquisitions/splits.
2. Compare random acquisition with uncertainty/diversity or task-cost strategies under equal labeling budgets. Make score calibration and representation identity explicit.
3. Prevent acquiring from the blind test set or using its outcomes to choose strategies. Track duplicate/entity coverage and distribution shift caused by selective sampling.
4. Handle annotation disagreement, abstention and reannotation with provenance. Version each pool/query/label snapshot and retraining checkpoint.
5. Evaluate learning curves versus labels/time/cost with repeated seeds and fixed test population. Stop according to a declared budget or improvement criterion.

## Acceptance evidence

Provide reproducible acquisition history, random baseline and budget-matched quality curves. Report annotator cost/disagreement and prove the blind set was excluded.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
