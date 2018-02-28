# Makefile

## Configuration

BUILD_TIME := $(shell date +%FT%T%z)
PROJECT    := $(shell basename $(PWD))

## Install dependencies
.PHONY: install
install:
	pipenv install --system

## Setup development environment
.PHONY: dev
dev:
	ln -sf config/dev.py app_config.py

## Setup production environment
.PHONY: prod
prod:
	ln -sf config/prod.py app_config.py
