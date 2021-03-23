# instagram_project3

django template


1) create virtualenv and activate create: python3 -m venv venv activate: .venv/bin/activate

2) pip install -r requairments.txt

3) create database postgress

create user "database user" with password 'your_super_secret_password';

alter role "database user" superuser ;

alter role "database user" with password 'your_super_secret_password';

alter role "database user" createrole createdb;

create database "database name" owner "database user";

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
