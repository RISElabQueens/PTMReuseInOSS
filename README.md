# PTMReuseInOSS

This repository accompanies our paper "Understanding the Use of Pre-trained Models in Open-source Software Projects".
It provides study materials, taxonomies, and reproducibility notes for our analysis of 401 GitHub projects.

**Research Questions**

RQ1: How do open-source projects structure and document their
PTM dependencies?
RQ2: What are the stages and their organization in the pipeline
of PTM-based open source projects?
RQ3: How do PTMs interact with other models?
**RQ Details**

RQ1 – PTM Structure and Documentation

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

