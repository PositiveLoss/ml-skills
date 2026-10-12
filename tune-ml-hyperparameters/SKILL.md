---
name: tune-ml-hyperparameters
description: "Design reproducible ML hyperparameter optimization. Use for Optuna/random/Bayesian search, pruning, nested CV, budget fairness, seed variance and avoiding test-set tuning."
---

# Tune ML hyperparameters

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Freeze independent validation/test units, objective, search budget and baseline. Parameterize ranges from meaningful scales and distinguish architectural from optimization changes.
2. Keep all fitted preprocessing inside each trial's training fold. Use nested CV when reporting performance of the entire tuned procedure.
3. Use reproducible trial identifiers/seeds and record failed/pruned trials. Compare algorithms under equivalent compute, data and evaluation budgets.
4. Validate pruning/early-stopping decisions with noisy or delayed learning curves. Avoid selecting best-of-many results on the final test set.
5. Refit the chosen configuration under the declared protocol, estimate seed/fold variability and evaluate the frozen candidate on blind test data.

## Acceptance evidence

Provide search space, budget, trial history and selection rule, including failures. Show objective evaluation does not touch test labels and pruning does not silently favor short/easy trials.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
