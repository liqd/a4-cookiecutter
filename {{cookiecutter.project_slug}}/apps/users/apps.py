from django.apps import AppConfig


class Config(AppConfig):
    name = 'apps.users'
    label = '{{cookiecutter.project_app_prefix}}_users'
