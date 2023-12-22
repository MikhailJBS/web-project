from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=500)
    url = models.URLField(blank=True)