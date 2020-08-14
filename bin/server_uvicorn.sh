#!/bin/bash

pipenv run uvicorn --host 0.0.0.0 --port 8000 --workers=10 --no-access-log --lifespan off benchmark.asgi:application
