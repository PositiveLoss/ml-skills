---
name: train-reinforcement-learning
description: "Implement and evaluate reinforcement learning experiments. Use for environment interfaces, terminated/truncated handling, reward design, policy/replay state, offline-data coverage and reproducible evaluation."
---

# Train reinforcement learning

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Specify environment, observation/action space, reward, safety constraints and deployment gap. Establish random/simple controller baselines and evaluation episodes/seeds.
2. Validate reset/step, shapes, action bounds and episode termination. Distinguish true termination from time-limit truncation when computing bootstrapped targets.
3. Record exploration, replay buffer, optimizer, RNG and environment state needed for resume. Separate evaluation policy from exploratory training behavior.
4. Compare algorithms under equal environment steps/compute and multiple independent seeds. Inspect reward hacking, unstable returns and distribution shift; offline RL needs dataset action/state coverage analysis.
5. Evaluate fixed policies on held-out tasks/seeds and realistic simulators before device execution. Report return distribution and failure rates instead of best-seed return alone.

## Acceptance evidence

Provide hand-checkable environment transitions, termination-target tests and independent evaluation episode results. Do not infer physical-robot safety or sim-to-real success from a toy environment pass.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
