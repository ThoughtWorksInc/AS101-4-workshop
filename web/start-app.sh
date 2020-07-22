#!/bin/bash

while ! timeout 1 bash -c 'cat < /dev/null > /dev/tcp/postgres/5432 2>&1 > /dev/null'; do
    echo "Attempting to connect to postgres db"
    sleep 1
done

echo "connected!"

python /usr/src/app/create_db.py

/usr/local/bin/gunicorn -w 2 -b :8000 echo.app:app
