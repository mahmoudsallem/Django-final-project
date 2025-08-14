from django.contrib import admin

# Register your models here.
from .models import Property , PropertyImage , PropertyReview , Place , Category , PropertyBooking

admin.site.register(Property)
admin.site.register(PropertyImage)
admin.site.register(PropertyReview)
admin.site.register(Place)
admin.site.register(Category)
admin.site.register(PropertyBooking)