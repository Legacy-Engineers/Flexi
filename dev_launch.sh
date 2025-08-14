#!/usr/bin/env bash

# This script is used to launch the development server

if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    uv sync
fi

# Activate the virtual environment
source .venv/bin/activate

DEBUG=True python manage.py runserver