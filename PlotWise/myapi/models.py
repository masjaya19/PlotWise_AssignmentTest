from django.db import models

# Create your models here.
class geopoint (models.Model):
    latitude = models.FloatField()
    longtitude = models.FloatField()
    date = models.DateField(auto_now_add=True)
