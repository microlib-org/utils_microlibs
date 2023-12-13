#!/bin/bash

# Check if two arguments are provided
if [ $# -ne 2 ]; then
    echo "Error: Usage: $0 <host> <tmux_session_name>"
    exit 1
fi

# Assign arguments to variables
HOST="$1"
TMUX_SESSION_NAME="$2"

# SSH into the host and kill the tmux session
ssh "$HOST" "tmux kill-session -t '$TMUX_SESSION_NAME'"

echo "Tmux session '$TMUX_SESSION_NAME' terminated on host '$HOST'"
