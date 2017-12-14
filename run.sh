#!/bin/bash

virtualenv env
source env/bin/activate
pipenv install --system
gunicorn run
