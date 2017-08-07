#!/bin/bash
set -x

git clone https://github.com/minorg/trygit.git
# Make changes...
git push

# Other people make changes...
git pull
