from django.db import models

# Create your models here.
class About(models.Model):
    What_we_do = models.CharField(max_length=200)
    our_mission = models.TextField(max_length=10000, blank=True)
    our_goals = models.TextField(max_length=10000, blank=True)
    image = models.ImageField(upload_to='about_images/', blank=True, null=True)

    def __str__(self):
        return self.What_we_do
    


class FAQ(models.Model):
    Title = models.CharField(max_length=200)
    description = models.TextField(max_length=10000, blank=True)

    def __str__(self):
        return self.Title
    


