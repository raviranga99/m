from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^newpost/',views.newpost, name="newpost"),
    url(r'^l/',views.list,name="list"),
    url(r'^(?P<id>[0-9]+)/delete/$', views.post_delete,name="delete"),
    url(r'^(?P<id>[0-9]+)/update/$', views.update,name="update"),
]
