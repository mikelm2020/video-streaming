#!/usr/bin/env bash
# exit on error
set -o errexit

python -m pip install --upgrade pip
pip install -r requirements/prod.txt

cd video_streaming
python manage.py collectstatic --no-input
python manage.py migrate