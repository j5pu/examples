SHELL = /bin/bash
export MAKE_PARENT_PATH := $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
export MAKE_PARENT_NAME := $(shell basename $(MAKE_PARENT_PATH))

all: bootstrap

.PHONY: all echo usage bootstrap

echo:
	@echo MAKE_PARENT_PATH: $(MAKE_PARENT_PATH)
	@echo MAKE_PARENT_NAME: $(MAKE_PARENT_NAME)

usage:
	@echo "make usage|bootstrap"

bootstrap: macdev
	@make --directory=scripts/bootstrap bootstrap
packages:
	@make --directory=scripts/bootstrap packages