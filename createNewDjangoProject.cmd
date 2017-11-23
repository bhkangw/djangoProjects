REM NAVIGATE TO VIRTUALEN
cd documents
cd codingdojo
cd python
cd myenvironments
source djangoEnv/bin/activate
REM BACK TO WHERE YOU WANT TO CREATE PROJECT
cd .. to desktop
REM CREATE NEW DJANGO PROJECT
django-admin startproject <newproject>
cd <newproject>
mkdir apps
cd apps
touch __init__.py
django-admin startapp <first_app>
cd <first_app>
touch urls.py
mkdir templates
cd templates
mkdir <first_app>
cd <first_app>
touch index.html
REM RUNNING NEW DJANGO PROJECT
cd .. to project name level
python manage.py runserver
REM DON'T FORGET TO ADD THE FIRST APP TO SETTINGS
open editor
add <first_app> to settings.py
'apps.<first_app>'

REM ACTIVATE SESSION:
REM Need to be in same directory as manage.py file
python manage.py makemigrations
python manage.py migrate
python manage.py shell
from apps.APPNAME.models import Users