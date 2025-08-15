from django.shortcuts import render, redirect
from django.utils.text import slugify

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

    def get_object(self, queryset=None):
        queryset = queryset or self.get_queryset()
        requested_slug = self.kwargs.get('slug')
        try:
            return queryset.get(slug=requested_slug)
        except Property.DoesNotExist:
            # Fallback: find an object whose slugified name matches, and persist slug
            for candidate in queryset.filter(slug__isnull=True):
                if slugify(candidate.name) == requested_slug:
                    candidate.slug = requested_slug
                    try:
                        candidate.save(update_fields=['slug'])
                    except Exception:
                        pass
                    return candidate
            # If still not found, raise 404
            raise

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        # No pk in URL now; ensure object slug is set and canonical
        obj = self.object
        request_slug = kwargs.get('slug')
        if not obj.slug and request_slug:
            try:
                obj.slug = request_slug
                obj.save(update_fields=['slug'])
            except Exception:
                pass
        elif obj.slug and request_slug != obj.slug:
            return redirect(obj.get_absolute_url())
        return response