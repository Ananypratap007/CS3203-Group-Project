from django.db import models

# Create your models here.

class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    price = models.PositiveIntegerField(default = 0)
    picture = models.ImageField(upload_to = 'menu_images', null = True)
