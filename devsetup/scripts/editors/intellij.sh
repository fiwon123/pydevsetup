#!/bin/bash

# Verify
echo "Verifying if IntelliJ is already installed..."
version=$(idea --version)
status=$?

if [ $status -eq 0 ]; then
    echo "IntelliJ found version: $version"
else
    path_idea=$(where rider)
    status=$?
    if [ $status -eq 0 ]; then
        echo "Idea found: $path_idea"
        echo "Trying to add path to use idea command line."
        # remove last part
        path_idea="${path_idea%/*}"
        echo "export PATH="'"$PATH':/$path_idea'"' > ~/.bashrc
    else
        echo "Failed to find Idea, exit status: $status"
        echo "Press enter to continue..."
        read
        exit 1
    fi
fi

# Set up editor extensions
idea installPlugins com.intellij.grazie.pro

echo "Completed!"
echo "Press enter to continue..."
read