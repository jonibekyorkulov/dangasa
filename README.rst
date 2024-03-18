Dangasa
=======

Dangasa is an automated library that helps you quickly create CRUD (Create, Read, Update, Delete) operations in Django REST Framework. It only serves ready-made models.

Usage
-----

To use the Dangasa library, the user needs to follow these steps:

Installation
------------

First, install the following libraries:

.. code-block:: bash

    pip install dangasa

Creating a Project
------------------

To create a project, follow these steps: (the project being created must be named 'core')

.. code-block:: bash

    django-admin startproject core .

.. code-block:: bash

    python manage.py startapp home


Modifying settings.py
---------------------

Modify project settings as follows:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'home',
    ]

Creating Models in the home App
-------------------------------

Now let's create models in the home app:

.. code-block:: python

    from django.db import models

    class Contact(models.Model):
        name = models.CharField(max_length=100)
        email = models.EmailField()
        phone = models.CharField(max_length=15)
        message = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.name

Migrating Created Models
-------------------------

Migrate the created models:

.. code-block:: bash

    python manage.py makemigrations
    python manage.py migrate

Modifying urls.py
------------------

Modify project urls as follows:

.. code-block:: python

    from django.urls import path, include

    urlpatterns = [
        ...
        path('', include('home.urls')),
    ]


Using Dangasa
--------------

To use Dangasa, run:

.. code-block:: bash

    Dangasa <app_name> <model_name>

Current Status
--------------

.. code-block:: bash

    Dangasa home Contact

.. code-block:: bash
    
    python manage.py runserver
