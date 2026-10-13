---
name: use-ml-dtypes
description: "Select, integrate and validate ml_dtypes NumPy extensions for ML pipelines. Use for bfloat16, float8 variants, MX float4/float6, narrow integers, complex32/bcomplex32, dtype registration, casting, promotion, accumulation, serialization and framework interoperability failures."
---

# Use ml_dtypes

Read [ML evidence contract](references/evidence.md) before implementation and [dtype guidance](references/task.md) when choosing formats or debugging numerical and interoperability behavior.

## Workflow

1. Inspect dependency constraints and record Python, NumPy, ml_dtypes and consuming framework versions. Check available public exports in the installed release; do not assume upstream main matches a released wheel. Resolve framework requirements together rather than upgrading ml_dtypes alone.
2. Import `ml_dtypes` before resolving its dtype names through NumPy. Use its exported scalar classes for explicit array construction and `ml_dtypes.finfo` / `ml_dtypes.iinfo` for supported limits. Check the exact dtype, item size and strides rather than inferring behavior from a name or NumPy dtype kind.
3. Choose storage, compute and accumulation precision separately. Test rounding, underflow, overflow, special values and signed zero for the exact format. Widen sensitive reductions explicitly; validate operation output dtypes and mixed-type promotion instead of assuming IEEE behavior or automatic widening.
4. Compare cast-and-restored arrays with a float32/float64 reference under an explicit error budget. Include boundary values and representative task data; quantify finite-value errors and non-finite changes separately. For FP8/MX pipelines, verify scale generation, clipping and reconstruction in the actual consumer; a cast alone is not a quantization pipeline.
5. Exercise array handoffs, serialization and loading in the target framework/runtime. Verify values, shape, dtype and layout after each boundary. Use an explicit supported conversion when necessary and report its precision/copy cost. Do not infer GPU kernel, DLPack or export support from successful NumPy construction.
6. Measure actual bytes and target-runtime performance before claiming a memory or speed improvement. Keep sub-byte encoding width separate from byte-addressed NumPy storage. Record executed checks, unsupported operations and untested devices.

## CPU smoke example

Run in the project's resolved environment; install `ml_dtypes` and NumPy together with its existing framework constraints if absent.

```python
import ml_dtypes as mld
import numpy as np

print("numpy", np.__version__, "ml_dtypes", mld.__version__)
assert np.dtype("bfloat16") == np.dtype(mld.bfloat16)
limits = mld.finfo(mld.bfloat16)
print("bfloat16", limits.eps, limits.max)

source = np.array([0.0, -0.0, 0.5, 1.0, 2.0, 256.0], dtype=np.float32)
stored = source.astype(mld.bfloat16)
restored = stored.astype(np.float32)
np.testing.assert_array_equal(restored, source)
np.testing.assert_array_equal(np.signbit(restored), np.signbit(source))

values = np.ones(10000, dtype=mld.bfloat16)
wide_sum = values.sum(dtype=np.float32)
assert wide_sum == 10000.0
print("sum", float(values.sum()), "float32 accumulation", float(wide_sum))

narrow = np.array([-8, 0, 7], dtype=mld.int4)
assert mld.iinfo(mld.int4).min == -8
assert mld.iinfo(mld.int4).max == 7
assert narrow.itemsize == 1
assert narrow.nbytes == narrow.size
print("int4 storage bytes", narrow.nbytes)
```

## Acceptance evidence

Report the dependency versions, exact format, storage/compute/accumulator choices, numerical error budget, observed boundary behavior and target-consumer round trips. Distinguish CPU dtype checks from model-quality, accelerator and throughput validation. Preserve an explicitly supported fallback where the consumer cannot represent the requested format.
