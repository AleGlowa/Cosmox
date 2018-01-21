from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView

from cosmox.models import Galaxy, PlanetarySystem, Planet
from cosmox.api.serializers import GalaxySerializer, PlanetarySystemSerializer, PlanetSerializer

class GalaxyListAPIView(ListAPIView):
    queryset = Galaxy.objects.all()
    serializer_class = GalaxySerializer

class PlanetarySystemListAPIView(ListAPIView):
    queryset = PlanetarySystem.objects.all()
    serializer_class = PlanetarySystemSerializer

class PlanetListAPIView(ListAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

# Wypisz informacje o konkretnej galaktyce(systemie, planecie)
class GalaxyDetailAPIView(RetrieveAPIView):
    queryset = Galaxy.objects.all()
    serializer_class = GalaxySerializer

# Zaktualizuj dane
class GalaxyUpdateAPIView(UpdateAPIView):
    queryset = Galaxy.objects.all()
    serializer_class = GalaxySerializer

# Usuń dane
class GalaxyDeleteAPIView(DestroyAPIView):
    queryset = Galaxy.objects.all()
    serializer_class = GalaxySerializer

# Wstaw nowe dane
class GalaxyCreateAPIView(CreateAPIView):
    queryset = Galaxy.objects.all()
    serializer_class = GalaxySerializer
