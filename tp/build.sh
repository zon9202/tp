#!/usr/bin/env bash
set -o errexit

pwd
ls
which python
which pip

python --version
pip --version

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate