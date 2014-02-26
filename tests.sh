#!/bin/bash
nosetests

cd web
python manage.py test
