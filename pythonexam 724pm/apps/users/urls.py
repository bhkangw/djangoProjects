from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.index),
    url(r'^$', views.dashboard),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^logout$', views.logout),
    url(r'^(?P<id>\d+)$', views.show),
    url(r'^(?P<id>\d+)/edit$', views.edit),
    url(r'^(?P<id>\d+)/destroy$', views.destroy),
    url(r'^(?P<id>\d+)/update$', views.update),
]
