from django.conf.urls import url

from Tartan import views

urlpatterns = [
    url(r'^detailed/(?P<imgid>[0-9]+)/$', views.imageDetail, name='imageDetail'),
    url(r'^album/(?P<albumid>[0-9]+)/$', views.albumDetail, name='albumDetail'),
    url(r'^detailed/(?P<imgid>[0-9]+)/info.json$', views.imageJsonInfo, name='imageJsonInfo'),
    url(r'^$', views.overview, name='albumIndex'),
]