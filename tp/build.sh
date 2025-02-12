echo #!/usr/bin/env bash
echo # exit on error
echo set -o errexit
echo pip install -r requirements.txt
echo python manage.py collectstatic --no-input
echo python manage.py migrate > build.sh