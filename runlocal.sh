#!/bin/bash

virtualenv env
source env/bin/activate
export ENVIRONMENT="dev"
gunicorn wsgi:app
