PROJECT := src/sucre

VENV := .venv
REPORTS := .reports

TESTS := tests
PY_FILES := $(shell find $(PROJECT) $(TESTS) -name "*.py")

clean:
	@rm -rf .mypy_cache
	@rm -rf .pytest_cache
	@rm -rf .coverage
	@rm -rf $(REPORTS)
	@rm -rf $(VENV)

$(VENV):
	pdm install

$(REPORTS):
	mkdir $(REPORTS)

setup: $(VENV) $(REPORTS)

flake: setup
	pdm run flake8 --max-complexity=10 $(PROJECT) $(TESTS)

bandit: setup
	pdm run bandit -rq $(PROJECT) $(TESTS)

isort: setup
	pdm run isort $(PROJECT) $(TESTS)

isort-lint: setup
	pdm run isort -c $(PROJECT) $(TESTS)

trailing: setup
	@pdm run add-trailing-comma $(PY_FILES) --exit-zero-even-if-changed

trailing-lint: setup
	@pdm run add-trailing-comma $(PY_FILES)

test: setup
	pdm run pytest --cov=$(PROJECT) --cov-branch

format: isort trailing

lint: flake bandit isort-lint trailing-lint

all: format lint test

.DEFAULT_GOAL := all
