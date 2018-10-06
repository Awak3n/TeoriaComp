#!/bin/bash

git add .
echo commit message:
read var
git commit -m $var
git checkout master
git pull
git checkout dev
git merge dev master
git checkout master
git merge master dev
git push
git checkout dev
