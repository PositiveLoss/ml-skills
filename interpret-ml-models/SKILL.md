---
name: interpret-ml-models
description: "Interpret and inspect ML models through controlled predictive analyses. Use for feature importance, permutation, PDP/ICE, SHAP-like explanations, counterfactual checks, correlated features and model reliance audits."
---

# Interpret ML models

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Define the explanatory question, audience, baseline population and output scale. Separate model behavior from claims about the real-world data-generating process.
2. Inspect feature/label lineage and confounders before importance plots. Compute importance on held-out data with the correct scoring metric and sample dependence.
3. Compare permutation/ablation and local explanations; evaluate correlated features and extrapolation introduced by synthetic perturbations.
4. Test explanation stability across model seeds, background samples and deployment slices. Check whether simple surrogate explanations actually approximate the relevant predictions.
5. Communicate assumptions and limitations, and use findings to design data/model checks. Validate actionable recommendations with appropriate causal evidence separately.

## Acceptance evidence

Provide reproducible held-out explanation artifacts, correlation sensitivity and at least one falsification/ablation check. Avoid interpreting importance ranking as causal effect or fairness certification.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
