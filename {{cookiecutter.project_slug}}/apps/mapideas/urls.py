from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'create/module/(?P<slug>[-\w_]+)/$',
        views.MapIdeaCreateView.as_view(), name='mapidea-create'),
    url(r'^(?P<slug>[-\w_]+)/edit/$',
        views.MapIdeaUpdateView.as_view(), name='mapidea-update'),
    url(r'^(?P<slug>[-\w_]+)/delete/$',
        views.MapIdeaDeleteView.as_view(), name='mapidea-delete'),
    url(r'^(?P<slug>[-\w_]+)/$',
        views.MapIdeaDetailView.as_view(), name='mapidea-detail'),
]
