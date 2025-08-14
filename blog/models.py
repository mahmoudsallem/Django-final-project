from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts_author')
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=15000, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='posts_category')
    tags = TaggableManager()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)  
    slug = models.SlugField(null=True, blank=True)
    


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Post, self).save(*args, **kwargs) # Call the real save() method


    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=200)



    def __str__(self):
        return self.name