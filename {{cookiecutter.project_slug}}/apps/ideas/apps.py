from django.apps import AppConfig


class Config(AppConfig):
    name = 'apps.ideas'
    label = '{{ cookiecutter.project_app_prefix }}_ideas'
