#!/bin/sh

# ./github.sh to push to GitHub
git status
git commit -a -m "added data"
git push -u origin main
