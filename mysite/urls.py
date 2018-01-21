from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url do aplikacji
    url(r'^cosmox/', include('cosmox.urls')),
    # url do rest api
    url(r'api/cosmox/', include('cosmox.api.urls'))
]

# W trybie debugowania zapisuj pliki medialne do katalogu media
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, documen_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
