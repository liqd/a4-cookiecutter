from rules.contrib.views import PermissionRequiredMixin

from adhocracy4.exports import mixins as a4_export_mixins
from adhocracy4.exports import views as a4_export_views

from . import models


class MapIdeaExportView(PermissionRequiredMixin,
                        a4_export_mixins.ItemExportWithLinkMixin,
                        a4_export_mixins.ExportModelFieldsMixin,
                        a4_export_mixins.ItemExportWithRatesMixin,
                        a4_export_mixins.ItemExportWithCategoriesMixin,
                        a4_export_mixins.ItemExportWithLabelsMixin,
                        a4_export_mixins.ItemExportWithCommentCountMixin,
                        a4_export_mixins.ItemExportWithLocationMixin,
                        a4_export_views.BaseItemExportView):
    model = models.MapIdea
    fields = ['name', 'description']
    html_fields = ['description']
    permission_required = '{{cookiecutter.project_app_prefix}}_mapideas.moderate_mapidea'

    def get_queryset(self):
        return super().get_queryset() \
            .filter(module=self.module)\
            .annotate_comment_count()\
            .annotate_positive_rating_count()\
            .annotate_negative_rating_count()

    def get_permission_object(self):
        return self.module

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated
