# PTMReuseInOSS


Software Dependencies 2.0: An Empirical Study of Reuse and Integration of Pre-Trained Models in Open-Source Projects
Jerin Yasmin · Wenxin Jiang · James C. Davis · Yuan Tian

**Overview**
This repository provides replication materials for our study of Pre-Trained Models (PTMs) in open-source software. PTMs are machine learning models trained in advance and reused across projects, introducing a new type of dependency: Software Dependencies 2.0.

We investigate how developers integrate PTMs, manage their reuse pipelines, and handle interactions with other models in OSS projects.

**Key Findings**
Multi-PTM reuse is common; models may be interchangeable (37%) or complementary (23%).

PTM dependency documentation is fragmented; only ~21% of projects document dependencies outside code.

Three PTM reuse pipeline types: Feature Extraction, Generative, Discriminative.

PTMs interact in modular or tightly coupled designs, reflecting pipeline complexity.

**Dataset**

Based on 401 GitHub repositories sampled from PeaTMOSS (28,575 repos using Hugging Face & PyTorch Hub PTMs).

Includes CSVs summarizing PTM usage, definitions, and references.

**Scripts**

Detect and trace PTM usage in OSS projects

Taxonomy: reuse pipelines and multi-model interactions

Generate plots
