# Dtype guidance

## Format selection

Treat `ml_dtypes` as NumPy dtype extensions, not an accelerator runtime or automatic mixed-precision policy. Inspect the installed module's public exports and the consumer's supported types before selecting a format.

| Family | Selection and validation guidance |
| --- | --- |
| `bfloat16` | Trade mantissa precision for an exponent range similar to float32; distinguish it from NumPy float16. Test tiny increments and reductions. |
| `float8_e3m4`, `float8_e4m3`, `float8_e5m2` | Compare exponent range and precision with `ml_dtypes.finfo`; test NaN and infinity handling. |
| `float8_e4m3fn`, `float8_e4m3b11fnuz`, `float8_e4m3fnuz`, `float8_e5m2fnuz` | Check each format's limits and encodings. Finite-only variants lack infinity; `fnuz` variants also lack negative zero. Do not reinterpret bytes between variants. |
| `float8_e8m0fnu` | Treat as an unsigned exponent-only scale format, with no zero or infinity and a NaN encoding; do not use as a general signed activation dtype. |
| `float4_e2m1fn`, `float6_e2m3fn`, `float6_e3m2fn` | Check availability and MX consumer requirements; these formats have neither infinity nor NaN and occupy a byte per NumPy element. |
| `int1`, `uint1`, `int2`, `uint2`, `int4`, `uint4` | Check availability and ranges with `ml_dtypes.iinfo`. These are unpacked byte-sized elements, not densely packed tensor buffers. |
| `complex32`, `bcomplex32` | Check availability and component access. Prefer the public `ml_dtypes.real` and `ml_dtypes.imag` helpers where present; test other complex operations individually. |

Use exported scalar classes or registered dtype names after importing `ml_dtypes`. Prefer the package's `finfo` and `iinfo` for its custom types; do not assume NumPy's built-in floating/integer classification or limit helpers handle every extension.

## Numerical checks

- Use an exactly representable fixture first, then evaluate real values near rounding ties, finite limits, the subnormal range and zero. Include infinities and NaNs only under a defined policy for formats that cannot represent them.
- Set accumulation dtype explicitly for sums and statistics. A reduction performed at storage precision can lose increments even when all inputs and the true result are in range. Compare against a wider reference on the same already-rounded inputs to isolate accumulation error from cast error.
- Test the actual mixed-dtype ufuncs and scalar/array combinations. Record the resulting dtype and observed cast behavior; avoid relying on a generic promotion hierarchy across frameworks or NumPy releases.
- Measure absolute and relative reconstruction error on finite values, with a defined near-zero denominator policy. Count newly non-finite outputs separately. Verify task metrics on held-out data before accepting a precision change.

## Runtime and artifact boundaries

Treat NumPy arrays, framework tensors and packed export formats as distinct contracts. Exercise the exact conversion APIs and relevant versions; unsupported types may raise errors, widen or require copies. Verify DLPack support in both producer and consumer rather than assuming all custom dtypes are registered.

Preserve logical dtype name, shape, layout, endianness and any scale/packing metadata with raw buffers. Test saved artifacts in a fresh process that imports `ml_dtypes` before dtype lookup, and confirm dtype and values after loading. If a format loses its logical identity through the selected serializer, choose a documented supported representation or an explicit conversion with a measured error budget.

For source builds, use the upstream build instructions and initialize required submodules. For binary import failures, inspect Python/NumPy wheel compatibility and the full dependency graph before changing versions. Treat upstream main, package metadata and installed releases as separate sources of evidence; historical README installation claims may lag metadata.

## Primary sources

- [Upstream format specifications, NumPy registration and arithmetic examples](https://github.com/jax-ml/ml_dtypes/blob/main/README.md)
- [Public exports, complex component helpers and version-dependent DLPack registration](https://github.com/jax-ml/ml_dtypes/blob/main/ml_dtypes/__init__.py)
- [Supported floating-point limits](https://github.com/jax-ml/ml_dtypes/blob/main/ml_dtypes/_finfo.py)
- [Supported integer limits](https://github.com/jax-ml/ml_dtypes/blob/main/ml_dtypes/_iinfo.py)
- [Dependency and build metadata](https://github.com/jax-ml/ml_dtypes/blob/main/pyproject.toml)

Recheck these sources against the installed release when implementing a task; do not interpret a dtype present on main as proof that a deployed environment supports it.
