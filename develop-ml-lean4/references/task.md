# Task reference

A proof about an ideal real-valued model does not establish floating-point implementation correctness or held-out accuracy. Lean FFI is version-sensitive; avoid passing arbitrary C structs by value as if supported. Prefer narrow validated data contracts and minimize trusted native code. Use the actual ML runtime as a testable boundary rather than treating its output as formal evidence.

Primary sources:
- https://lean-lang.org/doc/reference/latest/Run-Time-Code/Foreign-Function-Interface/
- https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/
