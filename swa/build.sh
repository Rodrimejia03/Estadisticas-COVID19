#!/usr/bin/env bash
# exit on error
set -o errexit

python install

python manage.py collectstatic --no-input
python manage.py migrate