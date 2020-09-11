echo "make migrations ...";
python manage.py makemigrations  

echo "running migrate ...";
python manage.py migrate 

echo "starting app ...";
python manage.py runserver 0.0.0.0:8002

