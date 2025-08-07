#!/bin/bash

# Activate the virtual environment
source ../myenv/bin/activate

# Run ruff formatter on the core/api directory
ruff format ./api

# Exit with ruff's exit code
exit $?