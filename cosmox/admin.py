from django.contrib import admin
from .models import Galaxy, PlanetarySystem, Planet

# Zapisz 3 tabele do widoku admina
admin.site.register(Galaxy)
admin.site.register(PlanetarySystem)
admin.site.register(Planet)
