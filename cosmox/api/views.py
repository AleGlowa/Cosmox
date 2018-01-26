from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView

from cosmox.models import Galaxy, PlanetarySystem, Planet
from cosmox.api.serializers import GalaxySerializer, PlanetarySystemSerializer, PlanetSerializer

class PlanetListAPIView(ListAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

class PlanetDetailAPIView(RetrieveAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

class PlanetUpdateAPIView(UpdateAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

class PlanetDeleteAPIView(DestroyAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

class PlanetCreateAPIView(CreateAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

class PlanetarySystemListAPIView(ListAPIView):
    queryset = PlanetarySystem.objects.all()
    serializer_class = PlanetarySystemSerializer

class PlanetarySystemDetailAPIView(RetrieveAPIView):
    queryset = PlanetarySystem.objects.all()
    serializer_class = PlanetarySystemSerializer

class PlanetarySystemUpdateAPIView(UpdateAPIView):
    queryset = PlanetarySystem.objects.all()
    serializer_class = PlanetarySystemSerializer

class PlanetarySystemDeleteAPIView(DestroyAPIView):
    queryset = PlanetarySystem.objects.all()
    serializer_class = PlanetarySystemSerializer

class PlanetarySystemCreateAPIView(CreateAPIView):
    queryset = PlanetarySystem.objects.all()
    serializer_class = PlanetarySystemSerializer

# Wypisz wszystkie galaktyki
class GalaxyListAPIView(ListAPIView):
    queryset = Galaxy.objects.all()
    serializer_class = GalaxySerializer

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
