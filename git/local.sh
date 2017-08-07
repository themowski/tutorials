#!/bin/bash
set -x

cd
rm -fr projects/minorg
mkdir projects
cd projects
mkdir minorg
cd minorg
git init

echo "File first line" >> file.txt
git add file.txt
git commit -m "First checkin"

echo "File second line" >> file.txt
git diff
git add file.txt
git status
git reset HEAD file.txt
git checkout -- file.txt
echo "File new second line" >> file.txt
git add file.txt
git commit -m "Second checkin"

git log

# git show

git rm file.txt
git status
git commit -m "Deleted file"

mkdir dir
git status
touch dir/file.txt
git status
git add dir
git status
git commit -m "Added subdirectory with file"

git mv dir/file.txt .
git status
git commit -m "Moved/renamed file"
