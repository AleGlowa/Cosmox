from django.conf.urls import url
from . import views

app_name = 'cosmox'

urlpatterns = [
    # /cosmox/ = strona główna
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /cosmox/<pk>/ = szczegółowa strona o galaktyce
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),

    # /galaxy/add/ = widok formularza do tworzenia nowego obiektu
    url(r'galaxy/add/$', views.GalaxyCreate.as_view(), name='galaxy-add'),

    # /galaxy/<pk>/ = widok formularza do aktualizowania obiektu
    url(r'galaxy/(?P<pk>\d+)/$', views.GalaxyUpdate.as_view(), name='galaxy-update'),

    # /galaxy/<pk>/delete/ = przekierowanie na chwilę do adresu po usunięciu obiektu
    url(r'galaxy/(?P<pk>\d+)/delete/$', views.GalaxyDelete.as_view(), name='galaxy-delete'),
]
