#!/bin/bash
echo " BUILD START "
python3.12 -m pip install --upgrade pip
python3.12 -m pip install -r requirements.txt
python3.12 manage.py collectstatic --noinput --clear

# Explicitly rename the static directory for Vercel
mv staticfiles dist

echo " BUILD END "
