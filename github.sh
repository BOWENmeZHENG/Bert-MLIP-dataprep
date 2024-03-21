#!/bin/sh

# ./github.sh to push to GitHub
git status
git commit -a -m "interactive annotation"
git push -u origin main
