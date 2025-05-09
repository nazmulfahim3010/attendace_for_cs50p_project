#!/bin/bash

# Optional: run your code (you can remove this line if not needed)
python3 project.py

# Stage all changes
git add .

# Commit with a timestamp message
git commit -m "Auto commit on $(date '+%Y-%m-%d %H:%M:%S')"

# Push to the current branch
git push
