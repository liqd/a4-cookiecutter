from django.utils.translation import ugettext as _
from rules.contrib.views import PermissionRequiredMixin

from adhocracy4.comments.models import Comment
from adhocracy4.exports import mixins as a4_export_mixins
from adhocracy4.exports import views as a4_export_views

from . import models


class IdeaExportView(PermissionRequiredMixin,
                     a4_export_mixins.ItemExportWithLinkMixin,
                     a4_export_mixins.ExportModelFieldsMixin,
                     a4_export_mixins.ItemExportWithRatesMixin,
                     a4_export_mixins.ItemExportWithCategoriesMixin,
                     a4_export_mixins.ItemExportWithLabelsMixin,
                     a4_export_mixins.ItemExportWithCommentCountMixin,
                     a4_export_views.BaseItemExportView):
    model = models.Idea
    fields = ['name', 'description']
    html_fields = ['description']
    permission_required = '{{cookiecutter.project_app_prefix}}_ideas.moderate_idea'

    def get_permission_object(self):
        return self.module

    def get_queryset(self):
        return super().get_queryset() \
            .filter(module=self.module)\
            .annotate_comment_count()\
            .annotate_positive_rating_count()\
            .annotate_negative_rating_count()

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()


class IdeaCommentExportView(PermissionRequiredMixin,
                            a4_export_mixins.ExportModelFieldsMixin,
                            a4_export_mixins.ItemExportWithLinkMixin,
                            a4_export_mixins.ItemExportWithRatesMixin,
                            a4_export_views.BaseItemExportView):

    model = Comment

    fields = ['id', 'comment', 'created']
    permission_required = '{{cookiecutter.project_app_prefix}}_ideas.moderate_idea'

    def get_permission_object(self):
        return self.module

    def get_queryset(self):
        comments = (Comment.objects.filter(idea__module=self.module) |
                    Comment.objects.filter(
                    parent_comment__idea__module=self.module))

        return comments

    def get_virtual_fields(self, virtual):
        virtual.setdefault('id', _('ID'))
        virtual.setdefault('comment', _('Comment'))
        virtual.setdefault('created', _('Created'))
        return super().get_virtual_fields(virtual)

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()