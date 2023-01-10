# Introduction
<!-- PROJECT LOGO -->
  <a href="https://github.com/dongtandung2001/Store-API">
    <img src="assets\djangoapi.png" alt="Logo">
  </a>


### Main features
Django Admin (CMS)

Buying product ( create cart, add item to cart, submit order)

Storing/Retrieve/Add new product

# Usage

Provide a basic online store API for storing/buying products.

After that just install the local dependencies, run migrations, and start the server.


# Online Store API

# Getting Started

First clone the repository from Github:

    $ git clone https://github.com/dongtandung2001/Store-API
    
Install project dependencies:

    $ pipenv install  

Activate the virtualenv for your project:

    $ pipenv shell

Then simply apply the migrations:

    $ python manage.py migrate
    
Populate database:

    $ python manage.py seed_db
Update password of your MySQL database in storefront/settings/dev

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront',
        'USER': 'root',
        'PASSWORD': 'Your database password'
    }
}
```

You can now run the development server:

    $ python manage.py runserver
