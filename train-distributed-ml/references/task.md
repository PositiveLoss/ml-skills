# Task reference

A mean of rank means is wrong when ranks have unequal sample/token counts. Validation sampler padding can duplicate examples and inflate metrics. FSDP checkpoint and API generations differ across releases. Gradient accumulation with unsynchronized steps must match the intended averaging and scheduler updates; document dropped/partial last batches.

Primary sources:
- https://docs.pytorch.org/docs/stable/distributed.html
- https://docs.pytorch.org/docs/stable/notes/ddp.html
