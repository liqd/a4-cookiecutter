from ckeditor_uploader import views as ck_views
from django.conf import settings
from django.conf.urls import include, url
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.views.i18n import javascript_catalog
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from django.contrib import admin

from rest_framework import routers

from adhocracy4.api import routers as a4routers
from adhocracy4.ratings.api import RatingViewSet
from adhocracy4.reports.api import ReportViewSet
from adhocracy4.comments.api import CommentViewSet

from apps.dashboard import urls as dashboard_urls
from apps.ideas import urls as ideas_urls
from apps.mapideas import urls as map_ideas_urls
from apps.projects import urls as project_urls

js_info_dict = {
    'packages': ('adhocracy4.comments',),
}

router = routers.DefaultRouter()
router.register(r'reports', ReportViewSet, base_name='reports')

ct_router = a4routers.ContentTypeDefaultRouter()
ct_router.register(r'comments', CommentViewSet, base_name='comments')
ct_router.register(r'ratings', RatingViewSet, base_name='ratings')


urlpatterns = [
    url(r'^django-admin/', include(admin.site.urls)),
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api/', include(ct_router.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^dashboard/', include(dashboard_urls)),
    url(r'^projects/', include(project_urls)),
    url(r'^ideas/', include(ideas_urls)),
    url(r'^mapideas/', include(map_ideas_urls)),
    url(r'^jsi18n/$', javascript_catalog,
        js_info_dict, name='javascript-catalog'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^upload/',
        login_required(ck_views.upload), name='ckeditor_upload'),
    url(r'^browse/', never_cache(ck_views.browse),
        name='ckeditor_browse'),
    url(r'', include(wagtail_urls))
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media locally
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    try:
        import debug_toolbar
    except ImportError:
        pass
    else:
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
