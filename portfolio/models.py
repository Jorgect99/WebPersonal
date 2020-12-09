from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 120)
    description = models.TextField(max_length = 255)
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)