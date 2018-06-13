from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'apps.users'
    label = '{{cookiecutter.project_app_prefix}}_users'
