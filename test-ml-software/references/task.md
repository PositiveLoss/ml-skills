# Task reference

A deterministic unit test cannot certify broad generalization. Avoid asserting exact stochastic scores across versions/devices. Tests that only compare the same serializer/decoder implementation can preserve a shared bug. Use independent golden inputs/outputs and test unsupported shapes explicitly.

Primary sources:
- https://docs.pytorch.org/docs/stable/notes/gradcheck.html
- https://scikit-learn.org/stable/common_pitfalls.html
