---
name: design-ml-losses
description: "Design, derive and validate ML objectives and losses. Use for logits vs probabilities, class weighting, masking, contrastive/ranking losses, regularization, normalization and gradient correctness."
---

# Design ML losses

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. State the prediction target, desired invariances, decision cost and label/mask semantics. Choose an objective connected to the task rather than a metric name alone.
2. Check input domain, logits/probabilities, class indices and reduction. Define whether averaging is by examples, valid tokens, pairs or weighted observations.
3. Derive expected behavior for perfect, wrong, empty/masked and extreme-logit cases. Implement stable numerical forms and avoid accidental double softmax/sigmoid.
4. Validate gradients with autograd and finite differences in float64 on a small problem. Check weighting/broadcasting and regularization scale across batch sizes.
5. Compare the new objective with the baseline using identical data/budgets, calibrated outputs where required and held-out task metrics.

## Acceptance evidence

Provide mathematical input/output contract, edge-case tests, finite-gradient evidence and a controlled ablation. Explain the gap between optimizing the surrogate loss and the deployed decision metric.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
