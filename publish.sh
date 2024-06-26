#!/bin/zsh

# Check if virtual environment is active, if not, activate it
if [[ -z "$VIRTUAL_ENV" ]]; then
  source .venv/bin/activate
fi

# Update pip
pip install --upgrade pip

# Update twine
pip install --upgrade twine

# Clean previous builds
rm -rf dist build service_collection.egg-info

# Build the package
python setup.py sdist bdist_wheel

# Upload the package to PyPI using Twine
twine upload dist/*

# Store exit code from twine
TWINE_EXIT_CODE=$?

# Clean up build artifacts
rm -rf dist build service_collection.egg-info

if [ $TWINE_EXIT_CODE -ne 0 ]; then
  echo "Package upload failed"
  exit 1
fi

if [ $TWINE_EXIT_CODE -eq 0 ]; then
  echo "Package uploaded successfully"
  exit 0
fi
