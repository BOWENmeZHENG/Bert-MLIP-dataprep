#!/bin/sh

# ./github.sh to push to GitHub
git status
git commit -a -m "annotate, same each individual record"
git push -u origin main
