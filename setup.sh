#!/bin/bash

virtualenv env
source env/bin/activate
make install && make dev
python manage.py initdb
