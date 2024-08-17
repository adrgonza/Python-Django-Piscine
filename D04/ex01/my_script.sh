#!/bin/bash

GITURL="https://github.com/jaraco/path.git"

/usr/bin/python3 -m venv venv
source venv/bin/activate

python -m pip --version

python -m pip install --log pip_install.log --force-reinstall git+$GITURL

python3 my_program.py