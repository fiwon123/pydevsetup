#!/bin/bash

# Set up VS Code extensions (if VS Code is used)
echo "Setting up VS Code extensions..."
code --install-extension ms-python.python
code --install-extension eamodio.gitlens

echo "Press enter to continue..."
read

# Any other editor setup can go here (VS Code, JetBrains, etc.)
