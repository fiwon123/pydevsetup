#!/bin/bash


# Verify
version=$(rider.bat --version)
status=$?

if [ $status -eq 0 ]; then
    echo "Rider found version: $version"
else
    path_rider=$(where rider)
    status=$?
    if [ $status -eq 0 ]; then
        echo "Rider found: $path_rider"
        echo "Trying to add path to use rider command line."
        # remove last part
        path_rider="${path_rider%/*}"
        echo "export PATH="'"$PATH':/$path_rider'"' > ~/.bashrc
    else
        echo "Failed to find Rider, exit status: $status"
        echo "Press enter to continue..."
        read
        exit 1
    fi
fi

# Set up editor extensions
rider.bat installPlugins tanvd.grazi

echo "Completed!"
echo "Press enter to continue..."
read