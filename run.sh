#!/bin/bash

virtualenv env
source env/bin/activate
python manage.py runserver
