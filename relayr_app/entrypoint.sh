#!/bin/bash
exec service nginx start  && gunicorn --config gunicorn_config.py app.app:app
