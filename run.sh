#!/bin/bash

# Ask user for venv location
read -p "Enter the location to create the virtual environment (e.g., C:/path/to/venv): " VENV_LOCATION

# Find an appropriate Python version (3.6 or higher)
PYTHON_VERSION=$(python3 -c "import sys; print('.'.join(map(str, sys.version_info[:2])))")

# Check if the Python version is 3.6 or higher
if [ $(echo "$PYTHON_VERSION >= 3.6" | bc -l) -ne 1 ]; then
    echo "Python version $PYTHON_VERSION is not supported. Please install Python 3.6 or higher and try again."
    exit 1
fi

# Create the virtual environment
python3 -m venv "$VENV_LOCATION/bard_chat_bot"

# Activate the virtual environment (Windows)
if [ "$OS" == "Windows_NT" ]; then
    source "$VENV_LOCATION/bard_chat_bot/Scripts/activate"
else
    source "$VENV_LOCATION/bard_chat_bot/bin/activate"
fi

# Install bardapi and tkinter
pip install bardapi==0.1.38 tkinter

# Deactivate virtual environment
deactivate

echo "Virtual environment 'bard_chat_bot' created and libraries installed successfully."
