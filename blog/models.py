from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts_author')
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=15000, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='posts_category')
    tags = TaggableManager()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)  


    def __str__(self):
        return self.title