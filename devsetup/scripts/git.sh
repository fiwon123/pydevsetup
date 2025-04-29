#!/bin/bash

# Set up Git config
echo "Configuring Git..."
git config --global user.name $1
git config --global user.email $2
git config --global init.defaultBranch main

# Add Git aliases (if desired)
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit

echo "Completed!"
echo "Press enter to continue..."
read