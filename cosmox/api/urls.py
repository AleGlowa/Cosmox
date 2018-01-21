from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.GalaxyListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.GalaxyDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.GalaxyUpdateAPIView().as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.GalaxyDeleteAPIView().as_view(), name='delete'),
    url(r'^create/$', views.GalaxyCreateAPIView().as_view(), name='create'),
]
