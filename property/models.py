from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='property_images/')
    description = models.TextField(max_length=10000, blank=True)
    location = models.ForeignKey('Place', on_delete=models.CASCADE, related_name='properties')    
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='properties')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return f"Image for {self.property.name}" 
    

class Place(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField(max_length=10000, blank=True)
    image = models.ImageField(upload_to='place_images/')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=10000, blank=True)

    def __str__(self):
        return self.name
    


class PropertyReview(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='reviews_property')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews_author')
    rating = models.IntegerField(default=0)
    feedback = models.TextField(max_length=10000, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Review for {self.property.name} by {self.author.username}"
    

count = (
    (1,1),
    (2,2),
    (3,3),
    (4,4)
)


class PropertyBooking(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='book_property')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='book_owner')
    date_from = models.DateTimeField(default=timezone.now)
    date_to = models.DateTimeField(default=timezone.now)

    guest = models.CharField(max_length=200, choices=count)
    children = models.CharField(max_length=200, choices=count)

    def __str__(self):
        return f"Booking for {self.property.name} by {self.user.username} from {self.date_from} to {self.date_to}"