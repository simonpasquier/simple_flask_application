#!/bin/sh
uwsgi --http 127.0.0.1:8000 --wsgi-file hello.py --callable app_dispatch
