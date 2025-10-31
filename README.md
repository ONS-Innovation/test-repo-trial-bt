# test-repo-trial-bt

[![Build Status](https://github.com/ONS-Innovation/test-repo-trial-bt/actions/workflows/ci.yml/badge.svg)](https://github.com/ONS-Innovation/test-repo-trial-bt/actions/workflows/ci.yml)
[![Build Status](https://github.com/ONS-Innovation/test-repo-trial-bt/actions/workflows/security-scan.yml/badge.svg)](https://github.com/ONS-Innovation/test-repo-trial-bt/actions/workflows/security-scan.yml)
[![Linting: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![poetry-managed](https://img.shields.io/badge/poetry-managed-blue)](https://python-poetry.org/)
[![License - MIT](https://img.shields.io/badge/licence%20-MIT-1ac403.svg)](https://github.com/ONS-Innovation/test-repo-trial-bt/blob/main/LICENSE)

test-repo-trial-bt

This project follows the Reproducible Analytical Pipeline (RAP) methodology, providing a modular ETL (Extract, Transform, Load) framework for data processing workflows.

**IMPORTANT**: This README was generated from a template.
Please update it with specific information about your project, including:

> - Detailed project description and purpose
> - Specific data sources and outputs
> - Usage examples and API documentation
> - Contributing guidelines specific to your project
> - Any project-specific compliance requirements

## RAP Methodology

This project implements RAP principles:

- **Reproducibility**: All processes are automated and version-controlled
- **Auditability**: Clear data lineage and transformation logic
- **Quality Assurance**: Automated testing and validation
- **Efficiency**: Reusable components and standardised workflows

---

## Table of Contents

[//]: # (:TODO: Enable link checking once https://github.com/tcort/markdown-link-check/issues/250 is resolved.)
<!-- markdown-link-check-disable -->
- [Getting Started](#getting-started)
    - [Pre-requisites](#pre-requisites)
    - [Installation](#installation)
    - [Running the RAP Pipeline](#running-the-rap-pipeline)
- [Development](#development)
    - [Run Tests with Coverage](#run-tests-with-coverage)
    - [Linting and Formatting](#linting-and-formatting)
    - [Security Scanning](#security-scanning)
    - [Type Checking](#type-checking)
- [RAP Components](#rap-components)
    - [Extract Module](#extract-module)
    - [Transform Module](#transform-module)
    - [Load Module](#load-module)
- [Contributing](#contributing)
- [License](#license)
<!-- markdown-link-check-enable -->

## Getting Started

To get a local copy up and running, follow these simple steps.

### Pre-requisites

Ensure you have the following installed:

1. **Python**: Version specified in `.python-version`.
2. **[Poetry](https://python-poetry.org/)**: This is used to manage package dependencies and virtual
   environments.
3. **Operating System**: MacOS

### Installation

1. Clone the repository and install the required dependencies.

```bash
git clone https://github.com/ONS-Innovation/test-repo-trial-bt.git
```

2. Install dependencies

[Poetry](https://python-poetry.org/) is used to manage dependencies in this project. For more information, read
the [Poetry documentation](https://python-poetry.org/).

To install all dependencies, including development dependencies, run:

```bash
make install-dev
```

To install only production dependencies, run:

```bash
make install
   ```

### Running the RAP Pipeline

The template includes several ways to run the ETL pipeline:

1. **Using the convenience function:**

```bash
make run
```

2. **Using individual components:**

```bash
# Extract data
poetry run python -c "from test_repo_trial_bt.extract import extract_from_source; print(extract_from_source('example_data.csv'))"

# Run full pipeline with custom parameters
poetry run python run_etl.py
```

3. **Programmatic usage:**

```python
from test_repo_trial_bt import ETLPipeline

pipeline = ETLPipeline()
success = pipeline.run_pipeline(
    source_path="data/input.csv",
    output_path="data/output.csv",
    apply_transforms=True
)
```

## Development

Get started with development by running the following commands.
Before proceeding, make sure you have the development dependencies installed using the `make install-dev` command.

A Makefile is provided to simplify common development tasks. To view all available commands, run:

```bash
make
```

### Run Tests with Coverage

The unit tests are written using the [pytest](https://docs.pytest.org/en/stable/) framework. To run the tests and check
coverage, run:

```bash
make test
```

To run only the unit tests, run:

```bash
make test-unit
```

To run only the end-to-end tests, run:

```bash
make test-e2e
```

### Linting and Formatting

[Ruff](https://github.com/astral-sh/ruff) is used for both linting and formatting of the Python code in this project.
Ruff is a fast Python linter and formatter that replaces multiple tools with a single, efficient solution.

The tool is configured using the `pyproject.toml` file.

To lint the Python code, run:

```bash
make lint
```

To auto-format the Python code and correct fixable linting issues, run:

```bash
make format
```

### Security Scanning

[Bandit](https://bandit.readthedocs.io/en/latest/) is used for security scanning of the Python code.
It helps identify common security issues in Python applications.

To run the security scan, run:

```bash
make security-scan
```

### Type Checking

[MyPy](https://mypy.readthedocs.io/) is used for static type checking to catch type-related errors before runtime.

To run type checking, run:

```bash
poetry run mypy test_repo_trial_bt
```

### GitHub actions

Linting/formatting and Security Scanning GitHub actions are enabled by default on template repositories. If you go to the `Actions` tab on your [repository](https://github.com/ONS-Innovation/test-repo-trial-bt/actions), you can view all the workflows for the repository. If an action has failed, it will show a red circle with a cross in it.

To find out more details about why it failed:

1. Click on the name of the action
2. Click the job in the Jobs section in the left sidebar
3. Find the dropdown with the red circle with a cross in it to view more information about the failed action

Please note that the GitHub actions will not automatically fix the errors, you must resolve them locally.

#### Pre-commit Hooks

The project includes pre-commit hooks to automatically run linting, formatting, and security checks before each commit.

1. Install **pre-commit** using Poetry:

```bash
poetry add --group dev pre-commit
```

2. Activate the git hooks:

```bash
pre-commit install
```

From now on Ruff and Bandit will run automatically on the files you stage before every commit.

## RAP Components

This template provides a modular ETL framework with the following components:

### Extract Module

The `extract.py` module contains the `DataExtractor` class and helper functions for reading data from various sources:

- **CSV files**: Primary data source with configurable parameters
- **File validation**: Ensures data sources exist before processing
- **Metadata extraction**: Provides file information and statistics
- **Error handling**: Comprehensive error management and logging

### Transform Module

The `transform.py` module contains the `DataTransformer` class for data cleaning and enhancement:

- **Data cleaning**: Removes duplicates and handles missing values
- **Calculated columns**: Adds derived fields based on business logic
- **Data filtering**: Applies configurable filters and business rules
- **Transformation logging**: Tracks all applied transformations
- **Column normalisation**: Standardises column names and formats

### Load Module

The `load.py` module contains the `DataLoader` class for outputting processed data:

- **Multiple formats**: CSV, Parquet, and JSON output support
- **Data summaries**: Automatic generation of processing metadata
- **Directory management**: Creates output directories as needed
- **Load validation**: Ensures successful data persistence
- **Performance tracking**: Monitors load operations and file sizes

### Pipeline Orchestration

The `__init__.py` module provides the `ETLPipeline` class that orchestrates the entire process:

- **End-to-end execution**: Manages extract, transform, and load phases
- **Configuration management**: Handles pipeline parameters and options
- **Error recovery**: Provides graceful error handling and rollback
- **Progress tracking**: Monitors pipeline execution and performance
- **Flexible execution**: Supports various execution patterns and customisation

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

See [LICENSE](LICENSE) for details.
