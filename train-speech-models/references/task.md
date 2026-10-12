# Task reference

The scorer reads JSONL sample_id/reference/hypothesis, applies explicit Unicode normalization plus optional lowercase, and reports corpus WER/CER and per-utterance edit counts. Empty-reference conventions and character-space inclusion are explicit in its output; no language-specific punctuation cleanup is hidden. Word error rate can exceed 1 due to insertions. It does not score diarization/VAD or prove telephony quality. Read references/tools.md.

Primary sources:
- https://huggingface.co/docs/transformers/tasks/asr
- https://huggingface.co/docs/transformers/model_doc/wav2vec2
- https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/intro.html
