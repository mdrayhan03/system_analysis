#!/bin/bash
echo " BUILD START "
python3.12 -m pip install --upgrade pip
python3.12 -m pip install -r requirements.txt

# Ensure static files are collected
python3.12 manage.py collectstatic --noinput --clear

# Ensure the target directory exists before moving
mkdir -p dist

# If staticfiles exist, move them to dist, otherwise print an error
if [ -d "staticfiles" ] && [ "$(ls -A staticfiles)" ]; then
    mv staticfiles/* dist/
    echo "Static files moved to dist/"
else
    echo "⚠️ WARNING: No static files found in 'staticfiles/'!"
fi

echo " BUILD END "
