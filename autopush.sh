#!/bin/bash

git add .
echo commit message:
read var
git commit -m $var

