from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import (FieldPanel, InlinePanel,
                                                PageChooserPanel)
from wagtail.core.models import Orderable
from wagtail.snippets.models import register_snippet


class MenuItem(models.Model):
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        related_name='+'
    )
    title = models.CharField(
        max_length=255, verbose_name="Title")

    @property
    def url(self):
        return self.link_page.url

    def __str__(self):
        return self.title

    panels = [
        PageChooserPanel('link_page'),
        FieldPanel('title')
    ]


@register_snippet
class NavigationMenu(ClusterableModel):

    menu_name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.menu_name

    panels = [
        FieldPanel('menu_name', classname='full title'),
        InlinePanel('menu_items', label="Menu Items")
    ]


class NavigationMenuItem(Orderable, MenuItem):
    parent = ParentalKey('cms_snippets.NavigationMenu', related_name='menu_items')
