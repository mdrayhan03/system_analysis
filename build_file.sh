#!/bin/bash
echo " BUILD START "
python3.12 -m pip install --upgrade pip
python3.12 -m pip install -r requirements.txt

# Collect static files into 'staticfiles'
python3.12 manage.py collectstatic --noinput --clear

# Create 'dist' directory and move static files there
mkdir -p dist
mv staticfiles/* dist/

echo " BUILD END "
