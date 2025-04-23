#!/bin/bash

SSH_KEY="$HOME/.ssh/id_ed25519"
# Check if SSH key already exists
if [[ -f "$SSH_KEY" && "$2" == "False" ]]; then
    echo "✅ SSH key already exists at $SSH_KEY"
    echo "Press enter to continue..."
    read
else
    email=$1

    echo "🔐 Generating a secure SSH key (ed25519)..."
    ssh-keygen -t ed25519 -C "$email" -f "$SSH_KEY"

    # Start ssh-agent
    eval "$(ssh-agent -s)"

    # Add the key to the agent
    ssh-add "$SSH_KEY"

    echo "✅ SSH key generated and added to ssh-agent!"
    echo "📋 Public key (add this to GitHub/GitLab):"
    echo ""
    cat "$SSH_KEY.pub"
    echo ""
    echo "Press enter to continue..."
    read
fi
