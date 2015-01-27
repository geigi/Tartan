from django.conf.urls import url

from PhotoGallery import views

urlpatterns = [
    url(r'^detailed/(?P<imgid>[0-9]+)/$', views.imageDetail, name='imageDetail'),
    url(r'^album/(?P<albumid>[0-9]+)/$', views.albumDetail, name='albumDetail'),
    url(r'^$', views.overview, name='albumIndex'),
]