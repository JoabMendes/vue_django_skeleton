## Vue + Django App Skeleton

## Requirements

- npm

- vue-cli

- pip

- python3

- python-dev-tools


## Build Setup

``` bash
# install dependencies
npm install

# build for production with minification
npm run build

# collect static files
./manage.py collectstatic

# apply migrations
./manage.py

# seed
./seed_dev.sh

# run python server
./manage.py runserver

```

## Running on dev

```
# Inside the project python environment, run the django server
./run_django_dev.sh

# In another terminal windown run the npm hot reloader serve
./run_npm_dev.sh

```

### npm default dependencies 

- vue
- vue-router
- bootstrap-vue
- vue-recaptcha
- vue-swal
- vue-multiselect

### django default dependencies

 - dj-database-url
 - Django
 - django-rest-recaptcha
 - django-webpack-loader
 - djangorestframework
 - flake8
 - gunicorn
 - psycopg2
 - pyflakes
 - PyYAML
 - requests
 - whitenoise

### New project setup 

    To do