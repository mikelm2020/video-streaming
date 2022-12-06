#!/usr/bin/env bash
# exit on error
set -o errexit

python -m pip install --upgrade pip
pip install -r requirements/requirements.txt

cd video_streaming
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py flush --noinput
python manage.py loaddata mydata.json