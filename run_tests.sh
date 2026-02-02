#!/bin/bash

# Exit immediately if any command fails
set -e

# Activate virtual environment
source venv/bin/activate

# Run tests
python -m pytest
