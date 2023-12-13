#!/bin/bash

# Check if five arguments are provided
if [ $# -ne 5 ]; then
    echo "Error: Usage: $0 <source_host> <destination_host> <source_directory> <destination_directory> <spec>"
    exit 1
fi

# Assign arguments to variables
SOURCE_HOST="$1"
DEST_HOST="$2"
SOURCE_DIR="$3"
DEST_DIR="$4"
SPEC="$5"

# Define the Python module
PYTHON_MODULE="llm_sepweight.filenames"

# Execute the Python command and loop over its output
for i in $(python -m $PYTHON_MODULE "$SPEC"); do
    # Perform the rsync operation via SSH
    ssh "$SOURCE_HOST" "rsync -avz --progress '$SOURCE_DIR/$i' '$DEST_HOST:$DEST_DIR/$i'"

    # Optional: Check if rsync was successful
    if [ $? -ne 0 ]; then
        echo "rsync failed for $i"
        # Decide how to handle the failure: exit, continue, etc.
    fi
done

echo "All rsync operations completed"
