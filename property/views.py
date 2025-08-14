from django.shortcuts import render, redirect

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

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        # Enforce canonical URL with slug only if object has a stored slug
        obj = self.object
        request_slug = kwargs.get('slug')
        if obj.slug:
            if request_slug != obj.slug:
                return redirect(obj.get_absolute_url())
        else:
            # If no slug stored yet, avoid redirect loops; optionally persist incoming slug
            if request_slug:
                try:
                    obj.slug = request_slug
                    obj.save(update_fields=['slug'])
                except Exception:
                    pass
        return response