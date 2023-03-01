#!/bin/sh
# Attempt migration until it suceeds (it takes some time for DB to spin up)
until python manage.py migrate
do 
    echo "Migration failed... Resetting"
    sleep 1
done
echo "Migration done, starting server"

if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL
fi

python manage.py runserver 0.0.0.0:8000