#!/usr/bin/env bash
# Git Automation Script
# Add all changes in the working directory to the staging area

git config --global user.email "abdosruor57@gmail.com"
git config --global user.name "aihassan1"

git add .
git commit -m "$*"
git push

# certbot certonly --standalone -d www.code-castle.tech --staple-ocsp -m abdosruor57@gmail.com --agree-tos
# sudo certbot certonly --standalone -d www.code-castle.tech --agree-tos -m abdosruor57@gmail.com
