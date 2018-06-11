from django.apps import AppConfig


class Config(AppConfig):
    name = 'cms'
    label = '{{cookiecutter.project_slug}}_cms'