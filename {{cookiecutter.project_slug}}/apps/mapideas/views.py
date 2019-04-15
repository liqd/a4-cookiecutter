from django.contrib import messages
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.views import generic
from rules.contrib.views import PermissionRequiredMixin

from adhocracy4.filters import views as filter_views
from adhocracy4.modules.models import Module
from adhocracy4.projects.mixins import ProjectMixin
from apps.ideas.filters import IdeaFilterSet

from . import forms
from . import models as idea_models


class MapIdeaListView(
    ProjectMixin,
    filter_views.FilteredListView
):
    model = idea_models.MapIdea
    paginate_by = 15
    filter_set = IdeaFilterSet

    def get_queryset(self):
        return super().get_queryset().filter(module=self.module) \
            .annotate_positive_rating_count() \
            .annotate_negative_rating_count() \
            .annotate_comment_count()


class MapIdeaDetailView(PermissionRequiredMixin, generic.DetailView):
    model = idea_models.MapIdea
    queryset = idea_models.MapIdea.objects.annotate_positive_rating_count() \
        .annotate_negative_rating_count()
    permission_required = '{{cookiecutter.project_app_prefix}}_mapideas.view_mapidea'

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_is_moderator'] = self.object.creator in self.object. \
            project.moderators.all()
        return context


class MapIdeaUpdateView(PermissionRequiredMixin, generic.UpdateView):
    model = idea_models.MapIdea
    form_class = forms.MapIdeaForm
    permission_required = '{{cookiecutter.project_app_prefix}}_mapideas.change_mapidea'

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.object.project
        context['mode'] = 'update'
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        module = self.object.module
        kwargs['module'] = module
        if module.settings_instance:
            kwargs['settings_instance'] = module.settings_instance
        return kwargs


class MapIdeaCreateView(PermissionRequiredMixin, generic.CreateView):
    model = idea_models.MapIdea
    form_class = forms.MapIdeaForm
    permission_required = '{{cookiecutter.project_app_prefix}}_mapideas.add_mapidea'

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()

    def dispatch(self, *args, **kwargs):
        mod_slug = self.kwargs[self.slug_url_kwarg]
        self.module = Module.objects.get(slug=mod_slug)
        self.project = self.module.project
        return super().dispatch(*args, **kwargs)

    def get_permission_object(self, *args, **kwargs):
        return self.module

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slug'] = self.module.slug
        context['project'] = self.project
        context['mode'] = 'create'
        return context

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.module = self.module
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['module'] = self.module
        if self.module.settings_instance:
            kwargs['settings_instance'] = self.module.settings_instance
        return kwargs


class MapIdeaDeleteView(PermissionRequiredMixin, generic.DeleteView):
    model = idea_models.MapIdea
    success_message = _("Your Idea has been deleted")
    permission_required = '{{cookiecutter.project_app_prefix}}_mapideas.change_mapidea'

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('project-detail',
                       kwargs={'slug': self.object.project.slug})
