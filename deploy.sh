#!/bin/bash

./setup.sh prod
git commit -am "Releasing..."
git push heroku master

./setup.sh dev
