#!/bin/bash

virtualenv env
source env/bin/activate
make install
python manage.py initdb
