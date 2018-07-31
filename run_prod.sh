python /code/manage.py migrate --noinput
python /code/manage.py createsu
python /code/manage.py loaddata company
python /code/manage.py runserver 0.0.0.0:8080
