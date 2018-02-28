#!/bin/bash

set -e

ENVIRONMENT=$1

if [[ $# -ne 1 ]]; then
  echo "Expecting ENVIRONMENT parameter."
  echo "Example:"
  echo "  ./setup.sh dev"
  echo "  ./setup.sh prod"
  exit 1
fi

ENVIRONMENT=$1

if [[ "$ENVIRONMENT" == "dev" || "$ENVIRONMENT" == "prod" ]]; then
  echo "Setting up $ENVIRONMENT environment"
else
  echo "Invalid environment. Valid environments: 'dev' or 'prod'"
  exit 1
fi

virtualenv env
source env/bin/activate
make install
make $ENVIRONMENT
python manage.py initdb
