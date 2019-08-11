#!/usr/bin/env bash

python3 flask-migrate.py db upgrade

gunicorn -b 0.0.0.0:9090 app:app