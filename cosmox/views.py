from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_list_or_404

from .models import Galaxy, PlanetarySystem, Planet

class IndexView(generic.ListView):
    template_name = 'cosmox/index.html'
    context_object_name = 'all_galaxies'

    def get_queryset(self):
        return Galaxy.objects.all()

class DetailView(generic.DetailView):
    model = Galaxy
    template_name = 'cosmox/detail.html'

class GalaxyCreate(CreateView):
    model = Galaxy
    fields = ['name', 'constellation', 'galaxy_type', 'diameter', 'num_of_starts',
              'mass', 'picture']

class GalaxyUpdate(UpdateView):
    model = Galaxy
    fields = ['name', 'constellation', 'galaxy_type', 'diameter', 'num_of_starts',
              'mass', 'picture']

class GalaxyDelete(DeleteView):
    model = Galaxy
    success_url = reverse_lazy('cosmox:index')
