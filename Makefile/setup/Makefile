.PHONY: venv vars clean clean-test clean-pyc clean-build docs help

.DEFAULT_GOAL := help

SHELL := $(shell command -v bash)

DIR := $(shell dirname "$(realpath $(firstword $(MAKEFILE_LIST)))")
DIRNAME := $(shell basename "$(DIR)")
DOCS := $(DIR)/docs
ENV := $(DIR)/.env
PACKAGE := $(DIRNAME)
PACKAGE_DIR := $(DIR)/$(DIRNAME)
ACTIVATE := $(DIR)/venv/bin/activate
SERVER := $(PACKAGE_DIR)/server
ANSIBLE := $(DIR)/$(DIRNAME)-ansible

export CONFLUENCE_PUBLISH := 0

ifneq ("$(wildcard $(ENV))","")
	ENV_EXISTS = 1
	include $(ENV)
	export
else
	@echo "Error: no .env file found at $(DIR)")
	ENV_EXISTS = 0
endif

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT
BROWSER := python3.7 -c "$$BROWSER_PYSCRIPT"

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

vault: ## check vault-password.text file
	@test -e "$(VAULT_PASSWORD_FILE)" || { echo "Error: no vault password file found '$(VAULT_PASSWORD_FILE)'"; exit 1; }

vars: venv ## print vars defined in make file
	@echo "SHELL: $(SHELL)"
	@echo "DIR: $(DIR)"
	@echo "DIRNAME: $(DIRNAME)"
	@echo "ENV: $(ENV)"
	@echo "ENV_EXISTS: $(ENV_EXISTS)"
	@echo "PACKAGE: $(PACKAGE)"
	@echo "PACKAGE_DIR: $(PACKAGE_DIR)"
	@echo "SERVER: $(SERVER)"
	@echo "CONFLUENCE_PUBLISH: $(CONFLUENCE_PUBLISH)"
	@source "$(ACTIVATE)" && echo "PATH: $$PATH"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

venv: ## create virtual environment
	@test -d $(DIR)/venv || python3 -m venv $(DIR)/venv

dev: venv  ## install requirements dev
	@source "$(ACTIVATE)" && python -m pip install --upgrade pip wheel setuptools
	@source "$(ACTIVATE)" && python -m pip install --upgrade $$( sort -u  $(DIR)/requirements/*.txt )

clean: clean-build clean-pyc clean-test clean-doc ## remove all build, test, coverage and Python package artifacts

clean-build: ## remove package build artifacts
	@rm -fr "$(DIR)"/build/
	@rm -fr "$(DIR)"/dist/
	@rm -fr "$(DIR)"/.eggs/
	@find "$(DIR)" -name '*.egg-info' -exec rm -fr {} +
	@find "$(DIR)" -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python package file artifacts
	@find "$(DIR)" -name '*.pyc' -exec rm -f {} +
	@find "$(DIR)" -name '*.pyo' -exec rm -f {} +
	@find "$(DIR)" -name '*~' -exec rm -f {} +
	@find "$(DIR)" -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage package artifacts
	@rm -fr "$(DIR)"/.tox/
	@rm -f "$(DIR)"/.coverage
	@rm -fr "$(DIR)"/htmlcov/
	@rm -fr "$(DIR)"/.pytest_cache

clean-doc: venv ## clean repository docs
	@rm -rf "$(DOCS)"/modules.rst "$(DOCS)"/$(PACKAGE).* "$(DOCS)"/_build "$(DOCS)"/_static
	@mkdir -p "$(DOCS)"/_build "$(DOCS)"/_static

lint: ## check package style with flake8
	@flake8 $(PACKAGE) tests

test: venv ## run package tests quickly with the default Python
	@source "$(ACTIVATE)" && pytest

test-all: venv ## run package tests on every Python version with tox {posargs:-U pip}
	@source "$(ACTIVATE)" && tox

coverage: venv ## check package code coverage quickly with the default Python
	@source "$(ACTIVATE)" && coverage run --source  -m pytest
	@source "$(ACTIVATE)" && coverage report -m
	@source "$(ACTIVATE)" && coverage html
	@$(BROWSER) htmlcov/index.html

docs: clean-doc ## generate repository Sphinx HTML documentation, including API docs
	@source "$(ACTIVATE)" && pip-compile --no-emit-index-url --output-file="$(DOCS)"/requirements.txt "$(DOCS)"/requirements.in
	@source "$(ACTIVATE)" && sphinx-apidoc -o "$(DOCS)" $(PACKAGE)
	@source "$(ACTIVATE)" && $(MAKE) -C "$(DOCS)" clean
	@source "$(ACTIVATE)" && $(MAKE) -C "$(DOCS)" html
	@source "$(ACTIVATE)" && $(BROWSER) "$(DOCS)"/_build/html/index.html

servedocs: docs ## compile repository docs watching for changes
	@source "$(ACTIVATE)" && cd "$(DOCS)" && watchmedo shell-command -p '*.rst' -c '$(MAKE) -C . html' -R -D .

confluence: clean-doc ## confluence docs
	@source "$(ACTIVATE)" && pip-compile --no-emit-index-url --output-file="$(DOCS)"/requirements.txt "$(DOCS)"/requirements.in
#	source "$(ACTIVATE)" && "$(VENV)"/sphinx-apidoc -o "$(DOCS)" $(PACKAGE)
	@source "$(ACTIVATE)" && $(MAKE) -C "$(DOCS)" clean
	@source "$(ACTIVATE)" && cd "$(DOCS)" && sphinx-build -b confluence . _build/confluence -E -a
	@source "$(ACTIVATE)" && $(BROWSER) "$(DOCS)"/_build/html/index.html
	@source "$(ACTIVATE)" && cd "$(DOCS)" && watchmedo shell-command -p '*.rst' -c '$(MAKE) -C . html' -R -D .

conf: clean-doc
	@source "$(ACTIVATE)" && $(MAKE) -C "$(DOCS)" clean
	@source "$(ACTIVATE)" && cd "$(DOCS)" && sphinx-build -b confluence . _build/confluence -E -a
	@source "$(ACTIVATE)" && $(BROWSER) "$(DOCS)"/_build/html/index.html

bump: clean ## repository bump2version updates version, git push
	@git add .
	@source "$(ACTIVATE)" && bump2version --allow-dirty patch
	@git push -u origin $$(git rev-parse --abbrev-ref HEAD) --tags

dist: bump ## builds source and wheel package
	@source "$(ACTIVATE)" && python setup.py sdist
	@source "$(ACTIVATE)" && python setup.py bdist_wheel
	@ls -l "$(DIR)"/dist

release: dist ## package and upload a release
	@source "$(ACTIVATE)" && twine upload dist/*

install: release ## install the package to the active Python's site-packages
	@$${PATH_PYTHON38}/python3.8 -m pip install --upgrade pip wheel setuptools $(PACKAGE)
