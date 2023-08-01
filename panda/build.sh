#!/usr/bin/env bash
# exit on error
set -o errexit

# poetry install
poetry add $( cat requirements.txt )

python manage.py collectstatic --no-input
python manage.py migrate