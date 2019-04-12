from django.db import models
from wagtail.admin import edit_handlers
from wagtail.core import blocks, fields
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel

from cms import blocks as cms_blocks


class HomePage(Page):
    body = fields.StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('call_to_action', cms_blocks.CallToActionBlock()),
        ('image_call_to_action', cms_blocks.ImageCallToActionBlock()),
        ('columns_text', cms_blocks.ColumnsBlock()),
        ('accordion', cms_blocks.DocsBlock())
    ])

    subtitle = models.CharField(max_length=120, blank=True)

    header_image = models.ImageField(blank=True)

    content_panels = [
        edit_handlers.FieldPanel('title'),
        edit_handlers.FieldPanel('subtitle'),
        ImageChooserPanel('header_image'),
        edit_handlers.StreamFieldPanel('body')
    ]

    subpage_types = ['cms_home.SimplePage']


class SimplePage(Page):
    body = fields.RichTextField(blank=True)

    content_panels = [
        edit_handlers.FieldPanel('title'),
        edit_handlers.FieldPanel('body'),
    ]

subpage_types = []
