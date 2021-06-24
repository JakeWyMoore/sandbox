from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 25)
    username = models.CharField(max_length = 25)
    password = models.CharField(max_length = 25)

class Images(models.Model):
    uploader = models.ForeignKey(User, related_name = 'user_images', on_delete = models.CASCADE, null = True)
    image = models.ImageField(default = 'default.png', blank = True, null = True)