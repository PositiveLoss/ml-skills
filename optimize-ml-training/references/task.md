# Task reference

Larger batches can alter optimizer behavior; AMP may change stability; checkpointing trades compute for memory. Increasing DataLoader workers/prefetch can move OOM from GPU to host. torch.compile/JAX JIT shape variation can trigger recompilation. A CPU microbenchmark does not predict accelerator throughput.

Primary sources:
- https://docs.pytorch.org/docs/stable/profiler.html
- https://docs.pytorch.org/docs/stable/amp.html
- https://docs.jax.dev/en/latest/benchmarking.html
