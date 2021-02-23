from django.db import models
from django.contrib import admin

# Create your models here.
class people(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
   
class peopleAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'photo')

class products(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    photo1 = models.ImageField(upload_to='photos1/')
   
class productsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'photo1') 
