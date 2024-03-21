#!/bin/sh

# ./github.sh to push to GitHub
git status
git commit -a -m "split_para '-'"
git push -u origin main
