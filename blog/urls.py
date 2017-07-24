

from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^simple',views.temp,name="t"),
    url(r'^asv',views.Aboutview.as_view()),
    url(r'^list',views.listv.as_view()),
    url(r'^blog/(?P<slug>[\w\-]+)/$', views.detailv.as_view(), name='detail_post_page'),

]
