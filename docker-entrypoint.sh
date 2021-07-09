#!/bin/bash

cd src;gunicorn -w 1 --bind :5000 app:app --timeout 250 --access-logfile -
