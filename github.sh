#!/bin/sh

# ./github.sh to push to GitHub
git status
git commit -a -m "a few new data"
git push -u origin main
