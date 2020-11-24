#!/bin/bash

python manage.py migrate
python manage.py loaddata test_users.json