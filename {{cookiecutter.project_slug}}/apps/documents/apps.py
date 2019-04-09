from django.apps import AppConfig


class Config(AppConfig):
    name = 'apps.documents'
    label = '{{ cookiecutter.project_app_prefix }}_documents'
