# Ansible managed
SHELL := bash
.DEFAULT_GOAL := all
THIS_FILE := $(lastword $(MAKEFILE_LIST))
words := $(shell wc --words requirements.txt | cut -d' ' -f1)
package := $(shell basename $$( pwd ))
version := $(shell grep '^__version__' version.py | cut -d '"' -f2 | cut -d '"' -f1)
pbr := $(shell grep "^pbr" requirements.txt > /dev/null 2>&1 && echo 1 || echo 0)
fluent-logger := $(shell grep "^fluent-logger" requirements.txt > /dev/null 2>&1 && echo 1 || echo 0)

all: devpi-upload

echo:
	@echo "Package: $(package)"
	@echo "Version: $(version)"

requirements: echo requirements.txt Dockerfile
ifneq ($(words),0)
	@echo "Prerequisite: requirements.txt valid"
else
	$(error Prerequisite: requirements.txt empty)
endif

wheels-rm:
	@echo "Prerequisite: requirements.txt removing wheels already in base"
ifneq ($(pbr),1)
	@echo "Prerequisite: requirements.txt removing wheels pbr"
	grep -v "^pbr" requirements.txt > /tmp/requirements.txt
	mv /tmp/requirements.txt requirements.txt
else
	@echo "Prerequisite: requirements.txt unchanged wheels pbr"
endif
ifneq ($(fluent-logger),1)
	@echo "Prerequisite: requirements.txt removing wheels fluent-logger"
	grep -v "^fluent-logger" requirements.txt > /tmp/requirements.txt
	mv /tmp/requirements.txt requirements.txt
else
	@echo "Prerequisite: requirements.txt unchanged wheels fluent-logger"
endif

build-dev: requirements { 'wheels-rm' if base_wheels_enable else '' }
	@echo "Starting: build-dev"
	@echo "Executing: docker build --target dev -t phones:dev --network attached ."
	docker build --target dev -t phones:dev --network attached .
	@$(MAKE) -f $(THIS_FILE) wheels-add

build-prod: requirements { 'wheels-rm' if base_wheels_enable else '' }
	@echo "Starting: build-prod"
	@echo "Executing: docker build -t phones:prod-$(version) -t $REGISTRY/phones:prod-$(version) --network attached ."
	docker build -t phones:prod-$(version) -t $REGISTRY/phones:prod-$(version) --network attached .
	@$(MAKE) -f $(THIS_FILE) wheels-add

push-prod: build-prod
	@echo "Starting: push-prod"
	@echo "Executing: docker push $REGISTRY/phones:prod-$(version)"
	docker push $REGISTRY/phones:prod-$(version)

devpi-upload: echo
	@echo "Starting: devpi-upload"
	@echo "Executing: pyup.bash"
	pyup.bash

devpi-push: echo
	@echo "Starting: devpi-push"
	@echo "Executing: pyup.bash push"
	pyup.bash push

wheels-add:
	@echo "Prerequisite: requirements.txt adding wheels already in base"
ifneq ($(pbr),1)
	@echo "Prerequisite: requirements.txt adding wheels pbr"
	echo pbr >> requirements.txt
else
	@echo "Prerequisite: requirements.txt unchanged wheels pbr"
endif
ifneq ($(fluent-logger),1)
	@echo "Prerequisite: requirements.txt adding wheels fluent-logger"
	echo fluent-logger >> requirements.txt
else
	@echo "Prerequisite: requirements.txt unchanged wheels fluent-logger"
endif
