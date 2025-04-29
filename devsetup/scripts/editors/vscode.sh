#!/bin/bash

# Verify
echo "Verifying if VS Code is already installed..."
version=$(code --version)
status=$?

if [ $status -eq 0 ]; then
    echo "VSCode found version: $version"
else
    path_vs_code=$(where rider)
    status=$?
    if [ $status -eq 0 ]; then
        echo "VS Code found: $path_vs_code"
        echo "Trying to add path to use code command line."
        # remove last part
        path_vs_code="${path_vs_code%/*}"
        echo "export PATH="'"$PATH':/$path_vs_code'"' > ~/.bashrc
    else
        echo "Failed to find VS Code, exit status: $status"
        echo "Press enter to continue..."
        read
        exit 1
    fi
fi

# Set up VS Code extensions (if VS Code is used)
echo "Setting up VS Code extensions..."
code --install-extension ms-python.python
code --install-extension eamodio.gitlens

echo "Completed!"
echo "Press enter to continue..."
read