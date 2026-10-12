---
name: train-speech-models
description: "Train and evaluate speech ML including ASR, LID, VAD and diarization. Use for Ukrainian/telephony audio, 8 kHz adaptation, speaker leakage, code switching, streaming/chunking and WER/CER/channel robustness."
---

# Train speech models

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

Read [executable helper](references/tools.md) before using the bundled script and fixtures.

## Workflow

1. Define ASR/LID/VAD/diarization task, audio sampling/channel/codec conditions and target language/code-switch population. Inspect transcripts, language labels and speaker/session identities.
2. Split by original recording/speaker/session as appropriate; keep segments and codec/augmentation variants together. Preserve truly unseen channel/codec and accented/cross-language slices.
3. Match resampling/filtering, normalization, tokenizer, blank/special labels and sequence lengths to the model. Upsampling 8 kHz does not restore missing high-frequency content.
4. Establish frozen-model/simple baselines, then train with aligned targets/masks and task-specific loss. For CTC verify input/target lengths and impossible alignments; for streaming define chunk/state/lookahead behavior.
5. Evaluate WER/CER or task-specific metrics with fixed normalization, speaker-cluster uncertainty and latency. Check code-switch, noise, accent, silence and short-utterance errors separately.

## Acceptance evidence

Run scripts/score_asr.py on hand-checkable transcript fixtures; report corpus denominators and normalizer. For real models provide speaker-held-out quality, channel slices and streaming-vs-offline behavior rather than toy-fixture scores.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
