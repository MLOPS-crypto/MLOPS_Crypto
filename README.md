# MLOPS Crypto

## Overview

**MLOPS Crypto** is an open‑source MLOps project designed to orchestrate end‑to‑end machine learning workflows for cryptocurrency models using **GitHub Actions** and **Google Vertex AI**.

The core of the project is **not a local training pipeline**, but an automated, cloud‑based workflow where GitHub Actions trigger Vertex AI jobs to:

* run training code,
* perform hyperparameter search,
* evaluate models,
* and deploy trained models.

All experiment outputs (logs, metrics, artifacts) are made available through **GitHub Actions artifacts**.

---

## Key Concepts

* **Configuration‑driven ML**: YAML configuration files control model parameters and hyperparameter search behavior.
* **CI/CD‑first MLOps**: GitHub Actions are the primary execution layer.
* **Cloud training**: Model training and deployment run on Vertex AI.
* **Reproducibility**: Pipelines are fully automated and version‑controlled.

---

## Features

* Hyperparameter search configured via `.yaml` files
* Automated training and deployment using Vertex AI
* GitHub Actions pipelines as the main execution engine
* Artifact collection for experiment results
* Dockerized execution environment
* Local pipeline validation via Makefile

---

## Tech Stack

* **Python**
* **Google Vertex AI** (training & deployment)
* **GitHub Actions** (pipeline orchestration)
* **Docker**
* **YAML** (pipeline and hyperparameter configuration)

---

## Configuration (YAML)

The project relies on **YAML configuration files** to control:

* Model hyperparameters
* Search spaces for hyperparameter optimization
* Training settings (epochs, batch size, etc.)

These files are consumed by the training code during pipeline execution and allow experiments to be modified **without changing source code**.

---

## GitHub Actions (Core Workflow)

GitHub Actions are the **heart of this project**.

The workflows:

1. Build the training environment
2. Submit a Vertex AI job
3. Execute training and hyperparameter search
4. Evaluate the model
5. Deploy the trained model
6. Upload results as GitHub Actions artifacts

### Artifacts

After each pipeline run, results are available directly in the **GitHub Actions artifacts**, which may include:

* Training logs
* Metrics
* Evaluation outputs
* Model references

---

## Local Development

### Purpose of the Makefile

The `Makefile` is **not used for production training**.

It exists only to:

* Run **local pipeline tests**
* Validate code before pushing changes


---

## Running the Project

This project is **not intended to be run locally end‑to‑end**.

To execute the full pipeline:

1. Push changes to the repository
2. Trigger the appropriate GitHub Actions workflow
3. Monitor execution in GitHub Actions
4. Retrieve results from workflow artifacts

---

## Contributing

Contributions are welcome.

Guidelines:

1. Fork the repository
2. Create a feature branch
3. Ensure pipelines pass locally (via Makefile)
4. Submit a Pull Request

---

## License

This project is released under the **HES-SO License**.

