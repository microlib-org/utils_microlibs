#!/bin/bash

# Check if five arguments are provided
if [ $# -ne 5 ]; then
    echo "Error: Usage: $0 <source_host> <destination_host> <source_filename> <dest_filename>"
    exit 1
fi

# Assign arguments to variables
SOURCE_HOST="$1"
DEST_HOST="$2"
SOURCE_FILENAME="$3"
DEST_FILENAME="$4"

ssh "$SOURCE_HOST" "rsync -avz --progress '$SOURCE_FILENAME' '$DEST_HOST:$DEST_FILENAME'"
