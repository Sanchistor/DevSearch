# DevSearch
Project to communicate with developers all over the world using Django

## Installation

1) Clone repository 'https://github.com/Sanchistor/DevSearch'
2) Create a virtual environment and activate   
> - `pip install virtualenv`
> - `virtualenv envname`
> - `envname\scripts\activate`
3) cd into project `cd DevSearch`
4) `pip install -r requirements.txt`
5) `python manage.py runserver`


## DB-postgresql setup
1) Go to `devsearch/settings.py`
2) Find variable `DATABASES`
3) Change to your local variables

        'NAME': 'Your name of DB',
        'USER': 'User of DB',
        'PASSWORD': 'Password of DB',
        'HOST': 'localhost',
        'PORT': '5432',
        
4) Run  `python manage.py migrate` to apply migrations
5) Run `python manage.py createsuperuser` to create admin and go to http://127.0.0.1:8000/admin/
