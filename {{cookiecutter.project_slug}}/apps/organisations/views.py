from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import ugettext_lazy as _
from django.views import generic

from adhocracy4.dashboard import mixins as a4dashboard_mixins

from apps.dashboard import forms
from apps.organisations import models


class DashboardOrganisationUpdateView(a4dashboard_mixins.DashboardBaseMixin,
                                      SuccessMessageMixin,
                                      generic.UpdateView):

    model = models.Organisation
    form_class = forms.OrganisationForm
    slug_url_kwarg = 'organisation_slug'
    success_message = _('Organisation successfully updated.')
    permission_required = '{{ cookiecutter.project_app_prefix }}_organisations.change_organisation'
    menu_item = 'organisation'

    def get_permission_object(self):
        return self.organisation
