#!/bin/sh

# ./github.sh to push to GitHub
git status
git commit -a -m "annotate"
git push -u origin main
