from django import forms
from django.utils.translation import ugettext as _

from adhocracy4.categories.forms import CategorizableFieldMixin
from adhocracy4.maps import widgets

from . import models


class MapIdeaForm(CategorizableFieldMixin, forms.ModelForm):

    class Meta:
        model = models.MapIdea
        fields = ['name', 'description', 'image', 'point', 'category']

    def __init__(self, *args, **kwargs):
        self.settings = kwargs.pop('settings_instance')
        super().__init__(*args, **kwargs)
        self.fields['point'].widget = widgets.MapChoosePointWidget(
            polygon=self.settings.polygon)
        self.fields['point'].error_messages['required'] = _(
            'Please locate your proposal on the map.')
        if self.fields['category']:
            self.fields['category'].empty_label = '---'
        else:
            del self.fields['category']
