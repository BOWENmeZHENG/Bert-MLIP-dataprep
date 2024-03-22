#!/bin/sh

# ./github.sh to push to GitHub
git status
git commit -a -m "fix ner naming"
git push -u origin main
