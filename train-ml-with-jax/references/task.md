# Task reference

JIT traces Python functions; side effects and captured values can behave differently from imperative expectations. A seed and a random key are not interchangeable with stateful framework RNG. Donation can invalidate input buffers. Sharding/export requirements differ across versions; consult the installed API and preserve shape/dtype contracts.

Primary sources:
- https://docs.jax.dev/en/latest/notebooks/Common_Gotchas_in_JAX.html
- https://docs.jax.dev/en/latest/random-numbers.html
- https://docs.jax.dev/en/latest/export/export.html
