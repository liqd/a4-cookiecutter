from django.views import generic


class ComponentLibraryView(generic.base.TemplateView):
    template_name = '{{cookiecutter.project_app_prefix}}_contrib/component_library.html'
