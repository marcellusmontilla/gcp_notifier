#!/bin/zsh
set -e


# Clean previous builds
rm -rf dist/*

# Build the package
python3 -m pip install --upgrade build twine
python3 -m build

echo "Uploading to TestPyPI..."
twine upload --repository testpypi dist/* --verbose

echo "TestPyPI deployment complete."
