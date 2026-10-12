# Task reference

The smoke helper uses a tiny synthetic classification task and checkpoint state held in memory; it does not load arbitrary files. Inspect actual torch version before using version-sensitive torch.amp, torch.compile, export or weights_only interfaces. Avoid checking GPU reproducibility by comparing CPU seeds alone. Read references/tools.md for usage.

Primary sources:
- https://docs.pytorch.org/docs/stable/autograd.html
- https://docs.pytorch.org/docs/stable/amp.html
- https://docs.pytorch.org/docs/stable/notes/serialization.html
