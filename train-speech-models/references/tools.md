# Executable helper

Python 3.10+ standard library.

Run from the skill directory, or use absolute script/asset paths; write outputs to an isolated project/scratch directory.

```sh
python scripts/score_asr.py assets/transcripts.jsonl
```

Use `--help` for argument definitions. Exit 0 means the requested check completed successfully; mismatch checks exit 1 and invalid input/options exit nonzero. The helper runs locally, downloads nothing, and does not execute model files. Sample data are synthetic/offline fixtures; their results establish tool behavior only. Read task.md for scope limits before applying the output to a model evaluation.

Length limits apply before and after Unicode normalization. `--max-edit-cells` bounds quadratic edit-distance work per utterance; increase it deliberately for long recordings, or split them using a documented evaluation protocol.
