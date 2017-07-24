

from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^login/',views.login_view),
    url(r'^register/',views.register_view),
    url(r'^logout/',views.logout_view,name='logout'),
    url(r'^wel/',views.welcome),
]
