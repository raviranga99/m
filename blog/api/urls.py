from django.conf.urls import url
from django.contrib import admin
from . import views
#from .views import (PostListAPIView,)

urlpatterns = [
    url(r'^$',views.PostListAPIView.as_view(), name='list'),
]
