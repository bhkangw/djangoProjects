from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show),
    url(r'^add/$', views.add),
    url(r'^books/(?P<id>\d+)$', views.review),
    url(r'^destroy/(?P<id>\d+)$', views.destroy),
    url(r'^(?P<id>\d+)$', views.user),
    # url(r'^dashboard$', views.dashboard),
]