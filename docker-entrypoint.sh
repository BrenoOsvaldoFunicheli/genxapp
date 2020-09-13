echo "Making migrations ..." && python manage.py makemigrations && echo "Running migrate ..." && python manage.py migrate && echo "Testing application" && python manage.py test && echo "Starting app ..." && python manage.py runserver 0.0.0.0:8002

# && python manage.py test