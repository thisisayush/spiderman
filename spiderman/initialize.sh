#!/bin/bash

echo "--- Making Migrations ---"
python manage.py makemigrations
python manage.py migrate

echo "--- Create Super User ---"
echo "+++ Please Enter Required Detils: +++"
python manage.py createsuperuser

echo "--- All Done! You can now start server by using: ---"
echo "python manage.py runserver"

