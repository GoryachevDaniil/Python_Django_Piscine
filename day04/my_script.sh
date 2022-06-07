#!/bin/sh
# python3 -m venv django_venv

source django_venv/bin/activate

# pip install django
# pip install requests

python3 -m pip install --force-reinstall -r requirement.txt

django-admin startproject
django-admin startapp ex0


python manage.py runserver