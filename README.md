# a4-cookiecutter

This is a Cookiecutter template to be used for Projects that need adhocracy4 and wagtail(optional).

## Create a new project

First you have to install Cookiecutter:

```
$ pip install cookiecutter
```
After that change to the directory where you want to create a your new Django project in.
Then set up the project using this cookiecutter template like so:

```
$ cookiecutter gh:liqd/a4-cookiecutter
```

## Next steps
Change into your newly created project directory and execute the following commands to get started.

Create virtual env, install requirements and create database with migrations:

```
$ make install
```
Create superuser:

```
$ venv/bin/python3 manage.py createsuperuser
```

Start server
```
$ make server
```






