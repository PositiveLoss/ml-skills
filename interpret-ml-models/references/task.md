# Task reference

Permutation importance reflects model reliance under the chosen permutation distribution, not intrinsic feature value. PDP can evaluate implausible feature combinations when variables correlate. Local attribution baselines and units change the result. Test explanations on known synthetic relationships before applying them to important decisions.

Primary sources:
- https://scikit-learn.org/stable/inspection.html
- https://scikit-learn.org/stable/modules/permutation_importance.html
- https://scikit-learn.org/stable/modules/partial_dependence.html
