# PTMReuseInOSS

This repository accompanies our paper "Understanding the Use of Pre-trained Models in Open-source Software Projects".
It provides study materials, taxonomies, and reproducibility notes for our analysis of 401 GitHub projects.

**Research Questions**

RQ1 – What PTMs are reused in OSS projects, and how are they sourced?

RQ2 – What stages and pipeline orientations characterize PTM reuse workflows?

RQ3 – How do PTMs interact with other models in practice?

**RQ Details**

RQ1 – PTM Identification

Collect 401 OSS projects.

Parse imports/dependencies and detect PTM sources (e.g., Hugging Face, TorchVision).

Classify PTMs by domain (CV, NLP, multimodal).

RQ2 – Reuse Pipelines

Annotate functional stages (INIT, ADPT, FEAT, FT, INF, POST, EVAL, DLV).

Group projects by organization of the stages: Feature Extraction, Generative, Discriminative.

RQ3 – Model Interactions

Review 145 survey papers for interaction patterns.

Analyze 200 multi-model projects.

Categorize interactions: Feature Handoff, Feedback, Evaluation, Post-Processing.

Repository Structure
data/        # Project list & annotations
taxonomy/    # Stage & interaction taxonomies
scripts/     # Parsing + analysis scripts
figures/     # Diagrams & workflow charts
README.md    # This file

