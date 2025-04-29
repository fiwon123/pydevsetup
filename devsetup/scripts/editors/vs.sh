#!/bin/bash

# Verify
version=$(vsixinstaller.exe --version)
status=$?

if [ $status -eq 0 ]; then
    echo "vsixinstaller found version: $version"
else
    path=$(where vsixinstaller)
    status=$?
    if [ $status -eq 0 ]; then
        echo "vsixinstaller found: $path"
        echo "Trying to add path to use vsixinstaller command line."
        # remove last part
        path="${path%/*}"
        echo "export PATH="'"$PATH':/$path'"' > ~/.bashrc
    else
        echo "Failed to find vsixinstaller, exit status: $status"
        echo "Press enter to continue..."
        read
        exit 1
    fi
fi


# Set up editor extensions
vsixinstaller.exe /q /a /i:Microsoft.VisualStudio.Package.Roslyn

echo "Completed!"
echo "Press enter to continue..."
read