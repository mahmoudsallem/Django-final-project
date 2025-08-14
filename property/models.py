from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='property_images/')
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=10000, blank=True)
    location = models.ForeignKey('Place', on_delete=models.CASCADE, related_name='properties')    
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='properties')
    created_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null=True, blank=True)
    


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super(Property, self).save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return str(self.name)
    

    def get_absolute_url(self):
        safe_slug = self.slug
        if not safe_slug:
            safe_slug = slugify(self.name) if self.name else str(self.pk)
        return reverse('property:property_detail', kwargs={'pk': self.pk, 'slug': safe_slug})

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return f"Image for {str(self.property.name)}" 
    

class Place(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='place_images/')

    def __str__(self):
        return str(self.name)

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=10000, blank=True)

    def __str__(self):
        return str(self.name)
    


class PropertyReview(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='reviews_property')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews_author')
    rating = models.IntegerField(default=0)
    feedback = models.TextField(max_length=10000, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Review for {str(self.property.name)} by {str(self.author.username)}"


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
        return f"Booking for {str(self.property.name)} by {str(self.user.username)} from {str(self.date_from)} to {str(self.date_to)}"