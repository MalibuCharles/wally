#Welcome to Wally 

Instructions to run the project

1. Clone the repository
2. Create your own virtual environment
- python3 -m venv venv
- source venv/bin/activate
3. Install your requirements
-pip install -r requirements.txt
4. Create a new PostgreSQL database
-- In your terminal:
- $ psql postgres
- $ CREATE DATABASE databasename
- $ \connect databasename
5.Go into pgAdmin, login, and check that the new database exists on the dbserver.
6. The database credentials to go in your project’s settings.py are the same credentials for pgAdmin.
7.settings.py
DATABASES = {
‘default’: {
‘ENGINE’: ‘django.db.backends.postgresql_psycopg2’,
‘NAME’: env(‘DATABASE_NAME’),
‘USER’: env(‘DATABASE_USER’),
‘PASSWORD’: env(‘DATABASE_PASS’),
}
}
8. Generate a new secret key
9. 6. Rename the project
10. 7. Make your migrations
-$ python manage.py makemigrations
-$ python manage.py migrate
11.Create a new superuser
- python manage.py createsuperuser
12. Run server
- python manage.py runserver
