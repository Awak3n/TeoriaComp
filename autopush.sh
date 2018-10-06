#!/bin/bash

echo commit message:
read var
git add .
git commit -m "$var"
git pull
git checkout dev
git merge dev master
git checkout master
git merge master dev
git push
git checkout dev
