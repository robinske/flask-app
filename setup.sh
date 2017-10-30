#!/bin/bash

set -e

export DATABASE_URL='postgresql://localhost:5432/boilerplate'
export SECRET_KEY='super-secret'

virtualenv env
source env/bin/activate
make install
python manage.py initdb
