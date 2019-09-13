#!/bin/sh


echo "users: i'm not doin shit if postgres doesn't have to..."

while ! nc -z users-db 5432; do
    sleep 0.1
done

echo "postgres: sorry i'm late. what's the plan :)"

python manage.py run -h 0.0.0.0
