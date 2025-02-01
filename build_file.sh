#!/bin/bash
echo "BUILD START"

# Install dependencies
python3.12 -m pip install --upgrade pip
python3.12 -m pip install -r requirements.txt

# Move assets to dist
mkdir -p dist
cp -r assets/* dist/

echo "BUILD END"
