from django.db import models
from django.contrib import admin
class Car(models.Model):
    brand_name=models.CharField()
    car_name=models.CharField(max_length=20)
    enginenum=models.IntegerField(max_length=10)
    release_date=models.DateField()

class CarAdmin(admin.ModelAdmin):
    list_display=('brand_name', 'car_name', 'enginenum', 'release_date')    
# Create your models here.
