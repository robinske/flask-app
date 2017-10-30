#!/bin/bash

virtualenv env
source env/bin/activate

export DATABASE_URL='postgresql://localhost:5432/boilerplate'
export SECRET_KEY='super-secret'

gunicorn wsgi:app
