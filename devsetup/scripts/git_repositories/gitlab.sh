#!/bin/bash

# Verify SSH
ssh -T git@gitlab.com

# Set remote URL for the repository (use SSH URL)
git remote set-url origin $1

# Verify the remote URL
git remote -v

echo "Press enter to continue..."
read