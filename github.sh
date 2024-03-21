#!/bin/sh

# ./github.sh to push to GitHub
git status
git commit -a -m "annotate, print para at '.'"
git push -u origin main
