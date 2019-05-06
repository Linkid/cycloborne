#!/bin/bash

read -p "Dev version (Y/n)?" -n 1 -r
echo

if [[ $REPLY =~ ^[Nn]$ ]]
then
    echo "prod"
    waitress-serve --call 'flaskr:create_app'
else
    echo "dev"
    export FLASK_APP=flaskr
    export FLASK_ENV=development
    flask init-db
    flask run
fi
