#!/bin/bash

# Install virtualenv
pip install virtualenv

# Create virtual environment
virtualenv venv

# Activate virtual environment
source ./venv/Scripts/activate

# Install requirements
pip install -r requirements.txt

# Deactivate virtual environment
deactivate

