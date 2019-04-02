#!/usr/bin/env bash

python /jwtauthexample/manage.py makemigrations
python /jwtauthexample/manage.py migrate
python /jwtauthexample/manage.py createsuperuser
python /jwtauthexample/manage.py runserver 0.0.0.0:8000