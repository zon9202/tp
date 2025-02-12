#!/bin/bash
set -o errexit
echo "Python version:"
python --version
echo "Pip version:"
pip --version
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate