#!/bin/bash

python3 -m venv django_venv
source django_venv/bin/activate

pip3 install --no-deps -r requirement.txt
