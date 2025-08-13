from django.db import models

# Create your models here.
class Settings(models.Model):
    site_name = models.CharField(max_length=200, unique=True)
    logo = models.TextField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    fb_link = models.URLField(max_length=200, blank=True, null=True)
    twitter_link = models.URLField(max_length=200, blank=True, null=True)
    instagram_link = models.URLField(max_length=200, blank=True, null=True)
    

    def __str__(self):
        return f"{self.site_name}: {self.logo}"

    class Meta:
        verbose_name = "Setting"
        verbose_name_plural = "Settings"