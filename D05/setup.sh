#!/bin/bash 

python3 -m venv venv

source venv/bin/activate

pip install django 

pip freeze > requirements.txt

django-admin startproject d05 .