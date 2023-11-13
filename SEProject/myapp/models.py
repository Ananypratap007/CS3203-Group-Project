from django.db import models

# Create your models here.

class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(default = 0, max_digits=4, decimal_places=2)
    picture = models.ImageField(upload_to = 'menu_images', null = True)

class EntreeItem(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(default = 0, max_digits=4, decimal_places=2)
    picture = models.ImageField(upload_to = 'menu_images', null = True)

class AppetizerItem(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(default = 0, max_digits=4, decimal_places=2)
    picture = models.ImageField(upload_to = 'menu_images', null = True)

class DesertItem(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(default = 0, max_digits=4, decimal_places=2)
    picture = models.ImageField(upload_to = 'menu_images', null = True)

class BeverageItem(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(default = 0, max_digits=4, decimal_places=2)
    picture = models.ImageField(upload_to = 'menu_images', null = True)

class SideItem(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(default = 0, max_digits=4, decimal_places=2)
    picture = models.ImageField(upload_to = 'menu_images', null = True)