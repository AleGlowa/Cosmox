#-*-coding:utf-8-*-
from django.db import models
from django.core.urlresolvers import reverse

class Galaxy(models.Model):
    name = models.CharField(max_length=50)
    constellation = models.CharField(max_length=50, null=True, blank=True)
    galaxy_type = models.CharField(max_length=50)
    diameter = models.CharField(max_length=50)
    num_of_starts = models.CharField(max_length=50)
    mass = models.CharField(max_length=50)
    picture = models.ImageField()

    def get_absolute_url(self):
        return reverse('cosmox:detail', kwagrs={'pk': self.pk})

    def __str__(self):
        if self.constellation:
            return self.name + ' w konstelacji ' + self.constellation
        else:
            return self.name + ' w żadnej konstelacji'

class PlanetarySystem(models.Model):
    # usuń system(y) planetarn(y/e), jeśli galaktyka jest usunięta
    galaxy = models.ForeignKey(Galaxy, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    constellation = models.CharField(max_length=50, null=True, blank=True)
    star_temperature = models.CharField(max_length=50)
    star_type = models.CharField(max_length=50)
    star_mass = models.CharField(max_length=50)
    star_radius = models.CharField(max_length=50)
    picture = models.ImageField()

    def __str__(self):
        if self.constellation:
            return self.name + ' w gwiazdozbiorze ' + self.constellation
        else:
            return self.name + ' w żadnym gwiazdozbiorze '

class Planet(models.Model):
    # usuń planet(ę/y), jeśli system jest usunięty (lub nie usuwaj gdy planeta nie była w żadnym układzie)
    planetary_system = models.ForeignKey(PlanetarySystem, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    picture = models.ImageField()
    mass = models.CharField(max_length=50)
    num_of_moons = models.PositiveIntegerField()
    planet_type = models.CharField(max_length=50)
    transit_time = models.CharField(max_length=50)
    rotation_period = models.CharField(max_length=50)
    distance_from_star = models.CharField(max_length=50)

    def __str__(self):
        if self.planetary_system:
            return self.name + '(' + self.planet_type + ')' + ' w systemie planetarnym ' + str(self.planetary_system)
        else:
            return self.name + '(' + self.planet_type + ')' + ' w żadnym systemie planetarnym'
