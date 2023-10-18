from django.db import models
from django.contrib import admin
class footballplayer (models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    country=models.CharField(max_length=20)
    position=models.CharField(max_length=20)
    experience=models.CharField(max_length=10)
class footballplayerAdmin(admin.ModelAdmin):
    list_display=('name','age','country','position','experience')


