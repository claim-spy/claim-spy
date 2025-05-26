# Claim Spy backend
This is the repo of the Claim Spy backend

# Build and run project

## Install UV
[Github link](https://github.com/astral-sh/uv)

## Create venv
`uv venv` to create the env

`source .venv/bin/activate` to activate the env

## Install dependencies
`uv sync`

## Migrate and create data
`python manage.py migrate`
`python manage.py createtiers`

## Start the server
`python manage.py runserver` 
