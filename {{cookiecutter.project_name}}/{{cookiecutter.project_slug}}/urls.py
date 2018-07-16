from ckeditor_uploader import views as ck_views
from django.conf import settings
from django.conf.urls import include, url
from django.views.i18n import javascript_catalog
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from adhocracy4.projects.decorators import user_is_project_admin
from django.views.decorators.cache import never_cache
from django.contrib import admin

js_info_dict = {
    'packages': ('adhocracy4.comments',),
}


urlpatterns = [
    url(r'^django-admin/', include(admin.site.urls)),
    url(r'', include(wagtail_urls)),
    url(r'^browse/', never_cache(user_is_project_admin(ck_views.browse)),
        name='ckeditor_browse'),
    url(r'^upload/',
        user_is_project_admin(ck_views.upload), name='ckeditor_upload'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^jsi18n/$', javascript_catalog,
        js_info_dict, name='javascript-catalog'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
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
