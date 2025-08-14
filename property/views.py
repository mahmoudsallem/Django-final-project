from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from property.models import Property


class PropertyList(ListView):
    model = Property
    template_name = 'property/property_list.html'
    context_object_name = 'properties'
    paginate_by = 10  # Number of properties per page

    def get_queryset(self):
        return Property.objects.all().order_by('-created_at')


class PropertyDetail(DetailView):
    model = Property
    template_name = 'property/property_detail.html'
    context_object_name = 'property'