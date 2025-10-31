# Architectural Decision Records

This directory contains Architectural Decision Records (ADRs) for the test-repo-trial-bt project.

## What are ADRs?

ADRs are documents that capture important architectural decisions made along with their context and consequences. They are a way to document the reasoning behind significant technical choices.

## ADR Index

1. [Package Manager Selection](./0001-package-manager.md) - Decision on using poetry for dependency management
2. [Linting and Code Quality Tools](./0002-linting-tools.md) - Selection of Ruff, MyPy, Bandit, and other code quality tools
3. [Testing Framework](./0003-testing-framework.md) - Decision to use pytest for testing

## Creating a New ADR

To create a new ADR:

1. Copy the template from `adr-template.md`
2. Name it with the next sequential number and a descriptive title, e.g., `0004-database-selection.md`
3. Fill in the sections with your decision information
4. Add it to this index
