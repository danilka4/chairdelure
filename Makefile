# Makefile by Chris Bonner and github/duarteocarmo

.PHONY: install clean lint format 

## Install for production
install:
	@echo ">> Installing dependencies"
	python -m pip install --upgrade pip
	python -m pip install -e .

## Install for development 
install-dev: install
	python -m pip install -e ".[dev]"

## Delete all temporary files
clean:
	rm -rf .ipynb_checkpoints
	rm -rf **/.ipynb_checkpoints
	rm -rf .pytest_cache
	rm -rf **/.pytest_cache
	rm -rf __pycache__
	rm -rf **/__pycache__
	rm -rf build
	rm -rf dist

## Lint using ruff
ruff:
	nbqa ruff .

## Format files using black
format:
	nbqa ruff . --fix
	nbqa black .

## Run tests
test:
	pytest --cov=src --cov-report xml --log-level=WARNING --disable-pytest-warnings

## Run checks (ruff + test)
check:
	ruff check .
	black --check .

## Build dependencies
build:
	pip-compile --resolver=backtracking --output-file=requirements.txt pyproject.toml
	pip-compile --resolver=backtracking --extra=dev --output-file=requirements-dev.txt pyproject.toml
