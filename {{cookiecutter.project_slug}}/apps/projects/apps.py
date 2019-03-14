from django.apps import AppConfig


class Config(AppConfig):
    name = 'apps.projects'
    label = '{{ cookiecutter.project_app_prefix}}_projects'
