# Machine learning skills — 56

A collection of 56 standalone agent skills covering machine learning development, evaluation, deployment and integration across nine programming languages. Skill instructions and references are written in English.

## Contents

- 56 skill directories, each with `SKILL.md` and `agents/openai.yaml` metadata.
- Task guidance and evidence requirements in each skill's `references/` directory.
- Python helpers, example data and upstream Hugging Face resources for selected skills.
- GitHub Actions workflows that validate the collection, build ZIP artifacts and package GitHub releases.

## Installation in Codex

Clone the repository or extract `machine-learning-skills.zip` from a release or a successful CI run. Copy the skill directories you want into the `skills` directory under `CODEX_HOME`, if configured. The default locations are:

- Linux/macOS: `~/.codex/skills/<skill-name>/SKILL.md`
- Windows: `%USERPROFILE%\.codex\skills\<skill-name>\SKILL.md`

Preserve each skill's `agents/`, `references/`, `scripts/` and example resources alongside `SKILL.md`. Place skill directories directly inside `skills/`, without an additional collection folder. Review any existing skill with the same name before replacing it. Refresh your Codex session after installation.

Invoke a skill explicitly, for example:

```text
Use $audit-ml-datasets to inspect this dataset for leakage and label quality.
Use $train-ml-with-pytorch to implement a reproducible training loop.
Use $export-ml-models to export this model and check inference parity.
```

Each skill provides its own instructions and references. Repository tooling in the root `scripts/`, `tests/` and `.github/` directories does not need to be installed.

## Validation and CI

Packaging requires Python 3.10 or later and PyYAML. Run these commands from the collection directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-ci.txt
python -B -m unittest discover -s tests -v
python -B scripts/release_skills.py --output dist/machine-learning-skills.zip
```

On Windows, create the environment with `py -3 -m venv .venv` and activate it with `.venv\Scripts\Activate.ps1` in PowerShell, then run the same `python` commands.

The packager discovers top-level directories containing `SKILL.md`, validates skill names, YAML descriptions, agent metadata and local Markdown resource links, then includes the README and skill resources at the ZIP root. Hidden files, Python caches, build output and root CI tooling are excluded. Packaging works from both a Git checkout and an extracted collection; it includes eligible files on disk, so review skill resources before distributing an archive.

CI runs on Linux, Windows and macOS for pushes, pull requests and manual dispatches using Python 3.14. It checks Python syntax, runs packaging regression tests and builds the ZIP. Download `machine-learning-skills.zip` from the workflow run's artifacts. Publishing a GitHub release runs the release workflow and attaches the same ZIP to that release.

## Validation limits

Packaging checks validate collection structure and archive contents. They do not train models or execute skill helpers. Individual helpers may require additional dependencies such as NumPy, scikit-learn or PyTorch; consult their skill instructions and tool references. Model quality, runtime compatibility, accelerator behavior and deployment performance need task-specific checks in the target environment.

## Catalog

### 1. Problem framing and data

- `frame-ml-problems` — Define prediction tasks, decision costs, baselines and success criteria.
- `audit-ml-datasets` — Inspect dataset quality, provenance, labels and leakage risks.
- `design-ml-data-splits` — Design splits that respect groups, time and deployment populations.
- `build-ml-feature-pipelines` — Build reproducible feature transformations for training and inference.
- `design-ml-losses` — Specify objectives, masking, weighting and gradient checks.
- `design-active-learning` — Plan annotation acquisition with label budgets and pool-bias checks.

### 2. Models and tasks

- `train-deep-learning-models` — Design architectures and controlled training experiments.
- `train-tabular-ml` — Train tabular baselines with leakage-safe preprocessing.
- `train-text-models` — Train text classifiers, extraction models and retrieval encoders.
- `train-vision-models` — Train image and video models with consistent augmentation and preprocessing.
- `train-speech-models` — Train and evaluate recognition, language identification and diarization.
- `train-time-series-models` — Build forecasting experiments with chronological backtesting.
- `train-anomaly-detectors` — Develop anomaly detection with appropriate thresholds and evaluation.
- `train-reinforcement-learning` — Implement reproducible policy training and environment evaluation.
- `build-ml-ranking-systems` — Develop retrieval, recommendation and ranking pipelines.

### 3. Training frameworks

- `train-ml-with-pytorch` — Implement training loops, autograd and resumable checkpoints.
- `train-ml-with-tensorflow` — Implement TensorFlow/Keras data pipelines, training and export.
- `train-ml-with-jax` — Implement JAX training with explicit state and transformation boundaries.

### 4. Adaptation and training efficiency

- `adapt-foundation-models` — Fine-tune pretrained models with task heads or adapters.
- `tune-ml-hyperparameters` — Compare search strategies within reproducible experiment budgets.
- `debug-ml-training` — Diagnose numerical failures, stalled learning and checkpoint problems.
- `optimize-ml-training` — Measure and improve training speed and memory use.
- `train-distributed-ml` — Implement sharding, synchronization and global metric aggregation.

### 5. Evaluation and testing

- `evaluate-ml-models` — Compare models using held-out metrics, uncertainty and quality slices.
- `calibrate-ml-predictions` — Calibrate probabilities, thresholds and abstention behavior.
- `interpret-ml-models` — Inspect model reliance through controlled predictive analyses.
- `test-ml-software` — Test preprocessing, gradients, serialization and serving contracts.

### 6. Reproducibility and pipelines

- `reproduce-ml-experiments` — Reproduce experiments with version, seed and artifact manifests.
- `track-ml-experiments` — Record runs, dataset lineage, metrics and model comparisons.
- `maintain-ml-pipelines` — Maintain versioned training, evaluation and release pipelines.

### 7. Deployment and operations

- `export-ml-models` — Export model artifacts and verify inference parity.
- `compress-ml-models` — Evaluate quantization, pruning and distillation tradeoffs.
- `serve-ml-models` — Build inference services with model lifecycle and resource controls.
- `deploy-edge-ml` — Integrate inference within device memory, latency and power budgets.
- `monitor-ml-models` — Track drift, delayed quality signals and rollout behavior.
- `secure-ml-artifacts` — Review model loading, provenance, privacy and artifact handling.

### 8. Programming language integration

- `develop-ml-python` — Integrate Python training orchestration and inference services.
- `develop-ml-c` — Integrate C inference APIs with explicit native resource ownership.
- `develop-ml-cpp` — Integrate C++ model runtimes and native training boundaries.
- `develop-ml-rust` — Implement Rust training or inference with runtime compatibility checks.
- `develop-ml-go` — Integrate Go inference services and native runtime bindings.
- `develop-ml-java` — Integrate JVM inference and model resource lifecycles.
- `develop-ml-kotlin` — Integrate Kotlin/JVM and Android model runtimes.
- `develop-ml-scala` — Integrate Spark ML pipelines and JVM native inference.
- `develop-ml-lean4` — Formalize ML invariants and bounded inference bridges in Lean 4.

### 9. Hugging Face ecosystem

These 11 skills are imported from the [Hugging Face Agent Skills documentation](https://huggingface.co/docs/hub/en/agents-skills) and [huggingface/skills](https://github.com/huggingface/skills) at revision `c3ff942be3e07116b475253f0a8fc4f54682c1a8`. Each imported directory includes its upstream resources, an Apache-2.0 `LICENSE.txt`, source provenance in `UPSTREAM.md`, and locally added Codex agent metadata. The documentation labels the Gradio skill `gradio`; its upstream directory and invocation name are `huggingface-gradio`.

- `hf-cli` — Download, upload and manage Hub repositories, resources and jobs with the `hf` CLI.
- `huggingface-datasets` — Explore dataset metadata, paginate rows, search text and apply filters.
- `huggingface-llm-trainer` — Train and fine-tune language models with TRL or Unsloth on Hugging Face Jobs.
- `huggingface-vision-trainer` — Train object detection, image classification and segmentation models.
- `huggingface-community-evals` — Evaluate Hub models on local hardware with inspect-ai and lighteval.
- `huggingface-trackio` — Log, visualize and monitor training experiments with Trackio.
- `huggingface-papers` — Find and read research paper pages and structured paper metadata.
- `huggingface-paper-publisher` — Publish and manage research papers on the Hub.
- `huggingface-tool-builder` — Build reusable scripts for Hugging Face API workflows.
- `huggingface-gradio` — Build Gradio web interfaces and demos in Python.
- `transformers-js` — Run models in JavaScript and TypeScript using WebGPU or WASM.
