---
name: frame-ml-problems
description: "Turn product or research goals into measurable machine-learning tasks. Use for classification/regression/ranking choices, baseline selection, data feasibility, decision costs, quality targets and experiment plans."
---

# Frame ML problems

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Identify the decision being made, prediction unit, available features at decision time, target construction and deployment population. Separate prediction from causal/intervention claims.
2. Translate business cost into measurable false-positive/negative, ranking or regression loss; specify abstention and human-review behavior. Make any requested percentage target refer to an exact metric and denominator.
3. Inspect label availability, coverage, latency, dataset permissions and realistic collection cost. Define train/validation/test populations and a no-model or simple statistical baseline.
4. Budget training/inference memory, latency, throughput and annotation effort. Decide whether supervised, unsupervised, retrieval, rules or an existing model is a justified starting point.
5. Write a bounded experiment plan with acceptance criteria, uncertainty requirements, stopped-run policy and known deployment mismatch. Avoid promising an accuracy threshold from architecture choice alone.

## Acceptance evidence

Provide a task/metric contract, baseline, sampling/split plan and cost/resource constraints. Identify missing labels or unobservable targets before starting expensive training.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
