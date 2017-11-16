from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_words$', views.add_words),
    url(r'^clear$', views.clear),
    # url(r'^random_word$', views.index),
    # url(r'^new$', views.new),
    # url(r'^create$', views.create),
    # url(r'^(?P<blog_id>\d+)$', views.show),
    # url(r'^(?P<blog_id>\d+)/edit$', views.edit),
    # url(r'^(?P<blog_id>\d+)/delete$', views.delete),
]