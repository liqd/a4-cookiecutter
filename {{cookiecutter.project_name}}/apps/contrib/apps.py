from django.apps import AppConfig


class Config(AppConfig):
    name = 'apps.contrib'
    label = '{{cookiecutter.project_app_prefix}}_contrib'