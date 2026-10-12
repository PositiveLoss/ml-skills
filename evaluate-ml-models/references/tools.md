# Executable helper

Python 3.10+ standard library.

Run from the skill directory, or use absolute script/asset paths; write outputs to an isolated project/scratch directory.

```sh
python scripts/evaluate_predictions.py assets/predictions.jsonl --bootstrap 200 --grouped --seed 17
```

Use `--help` for argument definitions. Exit 0 means the requested check completed successfully; mismatch checks exit 1 and invalid input/options exit nonzero. The helper runs locally, downloads nothing, and does not execute model files. Sample data are synthetic/offline fixtures; their results establish tool behavior only. Read task.md for scope limits before applying the output to a model evaluation.

The bundled prediction fixture is independent from audit-ml-datasets/assets/manifest.jsonl; their IDs cannot establish a shared held-out dataset. It has only three groups. The 200-draw example checks execution/repeatability, not reliable tail uncertainty. Increase draws and inspect interval stability for real evaluation, while remembering that additional draws cannot create additional independent groups.
