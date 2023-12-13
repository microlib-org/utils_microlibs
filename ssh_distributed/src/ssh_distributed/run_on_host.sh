#!/usr/bin/env bash

# Check if three arguments are provided
if [ $# -ne 3 ]; then
    echo "Error: Usage: $0 <host> <command> <tmux_session_name>"
    exit 1
fi

# Assign arguments to variables
HOST="$1"
COMMAND="$2"
TMUX_SESSION_NAME="$3"

# SSH into the host and execute the command in a new tmux session
ssh "$HOST" "tmux new-session -d -s '$TMUX_SESSION_NAME' '$COMMAND'"

echo "Command executed in tmux session '$TMUX_SESSION_NAME' on host '$HOST'"
