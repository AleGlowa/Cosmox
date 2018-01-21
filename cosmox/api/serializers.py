from rest_framework import serializers
from cosmox.models import Galaxy, PlanetarySystem, Planet

# Klasa serializująca dane(do wygodnego wysyłania i zapisywania danych z bazy)
class GalaxySerializer(serializers.ModelSerializer):

    class Meta:
        model = Galaxy
        fields = ('name', 'constellation', 'galaxy_type', 'diameter', 'num_of_starts',
                  'mass')

class PlanetarySystemSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlanetarySystem
        fields = ('galaxy', 'name', 'constellation', 'star_temperature', 'star_type',
                  'star_mass', 'star_radius')

class PlanetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Planet
        fields = ('planetary_system', 'name', 'mass', 'num_of_moons', 'planet_type',
                  'transit_time', 'rotation_period', 'distance_from_star')
