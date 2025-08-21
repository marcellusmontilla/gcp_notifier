#!/bin/zsh
set -e

# Remove any previous test environment
rm -rf venv-test

# Create a new virtual environment
python3 -m venv venv-test
source venv-test/bin/activate

# Upgrade pip and install the built wheel
pip install --upgrade pip
pip install dist/gcp_notifier-*.whl

# Test import and version
python -c "import gcp_notifier; print('gcp_notifier version:', getattr(gcp_notifier, '__version__', 'no __version__'))"

# Deactivate and clean up
deactivate
echo 'Test successful!'
