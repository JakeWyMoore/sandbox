from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    year = models.CharField(max_length=4)
    image = models.ImageField(default='default.png', blank = True)
