from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^galaxies/$', views.GalaxyListAPIView.as_view(), name='list'),
    url(r'^galaxies/(?P<pk>\d+)/$', views.GalaxyDetailAPIView.as_view(), name='detail'),
    url(r'^galaxies/(?P<pk>\d+)/update/$', views.GalaxyUpdateAPIView().as_view(), name='update'),
    url(r'^galaxies/(?P<pk>\d+)/delete/$', views.GalaxyDeleteAPIView().as_view(), name='delete'),
    url(r'^galaxies/create/$', views.GalaxyCreateAPIView().as_view(), name='create'),

    url(r'^systems/$', views.PlanetarySystemListAPIView.as_view(), name='list'),
    url(r'^systems/(?P<pk>\d+)/$', views.PlanetarySystemDetailAPIView.as_view(), name='detail'),
    url(r'^systems/(?P<pk>\d+)/update/$', views.PlanetarySystemUpdateAPIView().as_view(), name='update'),
    url(r'^systems/(?P<pk>\d+)/delete/$', views.PlanetarySystemDeleteAPIView().as_view(), name='delete'),
    url(r'^systems/create/$', views.PlanetarySystemCreateAPIView().as_view(), name='create'),

    url(r'^planets/$', views.PlanetListAPIView.as_view(), name='list'),
    url(r'^planets/(?P<pk>\d+)/$', views.PlanetDetailAPIView.as_view(), name='detail'),
    url(r'^planets/(?P<pk>\d+)/update/$', views.PlanetUpdateAPIView().as_view(), name='update'),
    url(r'^planets/(?P<pk>\d+)/delete/$', views.PlanetDeleteAPIView().as_view(), name='delete'),
    url(r'^planets/create/$', views.PlanetCreateAPIView().as_view(), name='create'),
]
