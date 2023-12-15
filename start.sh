#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

python BAKE/manage.py collectstatic --noinput
python BAKE/manage.py migrate --noinput
python BAKE/manage.py runserver 0.0.0.0:8000
#gunicorn BAKE.wsgi -b 0.0.0.0:8000 --chdir=/app --timeout 90
