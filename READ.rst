.. image:: https://badge.fury.io/py/test-todo.svg
    :target: https://badge.fury.io/py/test-todo

.. image:: https://coveralls.io/repos/github/nikhila05/Todo/badge.svg
	:target: https://coveralls.io/github/nikhila05/Todo

.. image:: https://travis-ci.org/nikhila05/Todo.svg?branch=master
    :target: https://travis-ci.org/nikhila05/Todo

.. image:: https://img.shields.io/pypi/dm/django-simple-pagination.svg
    :target: https://pypi.python.org/pypi/django-simple-pagination
    :alt: Downloads

.. image:: https://img.shields.io/pypi/v/django-simple-pagination.svg
    :target: https://pypi.python.org/pypi/django-simple-pagination
    :alt: Latest Release

.. image:: https://landscape.io/github/MicroPyramid/django-simple-pagination/master/landscape.svg?style=flat
   :target: https://landscape.io/github/MicroPyramid/django-simple-pagination/master
   :alt: Code Health

.. image:: https://img.shields.io/github/license/micropyramid/django-simple-pagination.svg
    :target: https://pypi.python.org/pypi/django-simple-pagination/


Django-Simple-Pagination
========================

Documentation_ -- GitHub_ -- Travis-CI_

Django-Simple-Pagination is a simple Django app to for digg-style pagination with little effort. `Django Simple Pagination`_.

Features:

- Dynamic blog articles
- Blog pages
- Contact us page (configurable)
- google analytics
- SEO compliant

Installation
--------------

- Install django-blog-it using the following command

.. code-block:: python

    pip install django-blog-it

    # or
    git clone git://github.com/micropyramid/django-blog-it.git

    cd django-blog-it

    python setup.py install

- Add app name in settings.py

.. code-block:: python

    INSTALLED_APPS = [
       '..................',
       'simple_pagination',
       'django_blog_it.django_blog_it',
       '..................'
    ]

- After installing/cloning this, add the following settings in the virtual env/bin/activate file to start discussions on blog articles

.. code-block:: python

	You can create your disqus account at https://disqus.com/profile/login/

    # Disquss details

    DISQUSSHORTNAME="Your Disquss Short Name"

    export DISQUSSHORTNAME


- Use virtualenv to install requirements

::

    pip install -r requirements.txt

You can try it by hosting on your own or deploy to Heroku with a button click.

Deploy To Heroku:

.. image:: https://www.herokucdn.com/deploy/button.svg
   :target: https://heroku.com/deploy?template=https://github.com/MicroPyramid/django-blog-it


Support
-------

We welcome your feedback and support, raise github ticket if you want to report a bug. Need new features?  contactus_


.. _contactus: https://micropyramid.com/contact-india/
.. _GitHub: https://github.com/nikhila05/Todo
.. _Travis-CI: https://travis-ci.org/nikhila05/Todo
.. _Django Simple Pagination: https://micropyramid.com/oss/
.. _Documentation: http://django-blog-it.readthedocs.io/en/latest/?badge=latest
