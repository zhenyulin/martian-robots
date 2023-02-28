## CONFIG
PYTHONPATH := $(PYTHONPATH):$(pwd)
SHELL := /bin/bash -v

## VARIABLES
VIRTUAL_ENV_NAME := $(shell poetry env info -p | rev | cut -d'/' -f1 | rev)

install:
	@poetry install

cleanup:
	@rm -rf **/__pycache__
	@poetry env remove $(VIRTUAL_ENV_NAME)

shell:
	@poetry shell

run:
	@poetry run python main.py

test:
	@poetry run pytest . -vv -s

test-watch:
	@watchman-make -p 'src/**/*.py' -r 'poetry run pytest src/ -vv -s'
