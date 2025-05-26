# Claim Spy backend
This is the repo of the Claim Spy backend

# Build and run project

## Create venv
uv venv
source .venv/bin/activate

## Install dependencies
uv sync

## Start the server
python manage.py runserver (si le virtual env est activé)
uv run python manage.py runserver (si le virtual env n'est pas activé)
