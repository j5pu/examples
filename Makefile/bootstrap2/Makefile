SHELL = /bin/bash
export MAKE_PARENT_PATH := $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
export MAKE_PARENT_NAME := $(shell basename $(MAKE_PARENT_PATH))

all: bootstrap

.PHONY: all bootstrap brew-bundle brew-dump pip npm ruby packages defaults dock

bootstrap: main.sh
	@./main.sh
brew-bundle:
	@brew bundle --file="$${BREWFILE}1"
brew-dump:
	@cd "$${BREWFILE}"
	@brew bundle dump
pip:
	@pip3 install --upgrade -r "$${REQUIREMENTS}"
npm:
	@npm install -g $( cat "$${NPMFILE}" )
ruby:
	@/usr/local/opt/ruby/bin/bundle --gemfile="$${GEMFILE}" --system
packages: brew-bundle pip npm ruby
defaults:  ../../../macdev
	@./defaults.sh
dock:  dock.sh
	@./dock.sh