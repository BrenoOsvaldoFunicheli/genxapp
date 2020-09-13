echo "Making migrations ..." && python manage.py makemigrations && echo "Running migrate ..." && python manage.py migrate && echo "Testing application" && python manage.py test



