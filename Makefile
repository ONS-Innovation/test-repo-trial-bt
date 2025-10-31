.DEFAULT_GOAL := all

.PHONY: all
all: ## Show the available make targets.
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@fgrep "##" Makefile | fgrep -v fgrep

.PHONY: clean
clean: ## Clean the temporary files.
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf .ruff_cache

.PHONY: format
format:  ## Format the code using Ruff.
	poetry run ruff format .
	poetry run ruff check . --fix

.PHONY: lint
lint:  ## Run all linters (ruff).
	poetry run ruff check .

.PHONY: security-scan
security-scan:  ## Run security scan using Bandit.
	poetry run bandit -r test_repo_trial_bt

.PHONY: test
test:  ## Run all the tests and check coverage.
	poetry run pytest -n auto --cov=test_repo_trial_bt --cov-report term-missing --cov-fail-under=50 tests/

.PHONY: test-unit
test-unit: ## Run the unit tests and check coverage.
	poetry run pytest -n auto --cov=test_repo_trial_bt --cov-report term-missing --cov-fail-under=50 tests/unit

.PHONY: test-e2e
test-e2e: ## Run the end-to-end tests.
	poetry run pytest tests/e2e

.PHONY: install
install:  ## Install the dependencies excluding dev.
	poetry install --only main

.PHONY: install-dev
install-dev:  ## Install the dependencies including dev.
	poetry install

.PHONY: run
run:
	poetry run python run_etl.py

