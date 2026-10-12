# ML evidence contract

Identify the prediction unit, target, decision cost, serving context and permitted data use. Inspect the existing implementation and lockfiles before changing frameworks. Record data version, code revision, model/config identity, seeds, dependency versions, device and precision. Confirm the installed API rather than treating a latest-documentation example as version independent.

Keep train, validation/calibration and final test responsibilities separate. Fit preprocessing, resampling, feature selection and learned vocabularies only inside training folds. Use group/time-aware splits for related examples; preserve a blind final holdout. Seed control alone does not ensure identical runs across framework versions, platforms or hardware.

Compare a simple baseline with the candidate on the same evaluation units. Choose metrics from the decision cost and class distribution; include denominator, slices, uncertainty and resource measurements. Resample independent units, such as speakers, sessions or users, when estimating uncertainty. State when a confidence interval assumes independence or is unstable with few groups. Do not infer causal effects from prediction quality or interpret correlations as intervention evidence.

Test data contracts, transformations, numerical behavior, artifact loading and serving lifecycle separately from model quality. Preserve preprocessing/tokenizer/label mappings with the model. Validate target-runtime predictions and supported shapes before calling an export successful. Treat model files and custom loading code as executable or otherwise untrusted inputs where appropriate; use verified sources and controlled loading.

Report executed commands and observed results. Distinguish CPU smoke tests, full training, GPU/distributed/device validation and production evidence. Do not claim a target quality or speed improvement without a matching held-out evaluation or measured benchmark. Keep generated reports and output directories outside the installed skill folder.

Primary guidance:
- https://scikit-learn.org/stable/common_pitfalls.html
- https://scikit-learn.org/stable/modules/cross_validation.html
- https://docs.pytorch.org/docs/stable/notes/randomness.html
