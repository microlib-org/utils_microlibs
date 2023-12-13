#!/bin/bash

# Check if two arguments are provided
if [ $# -ne 2 ]; then
    echo "Error: Usage: $0 <host> <tmux_session_name>"
    exit 1
fi

# Assign arguments to variables
HOST="$1"
TMUX_SESSION_NAME="$2"

# SSH into the host, find and kill the main process in the tmux session, then kill the tmux session
ssh "$HOST" "
    PID=\$(tmux list-panes -t '$TMUX_SESSION_NAME' -F '#{pane_pid}' | head -n 1);
    if [ -n \"\$PID\" ]; then
        kill \$PID;
    fi;
    tmux kill-session -t '$TMUX_SESSION_NAME';
"

echo "Tmux session '$TMUX_SESSION_NAME' and its main process terminated on host '$HOST'"
