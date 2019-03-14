from django import forms
from django.utils.translation import ugettext_lazy as _

from apps.organisations.models import Organisation


class OrganisationForm(forms.ModelForm):

    class Meta:
        model = Organisation
        fields = ['name']
        labels = {
            'name': _('Organisation name')
        }
