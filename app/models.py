from re import T
from django.db import models

# Create your models here.
class SiteUser(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.name} - {self.email} - {self.login}"
    
    
class Song(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    listening = models.PositiveIntegerField()
    album = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name} - {self.date} - {self.listening} - {self.album}"
    
    
class Concert(models.Model):
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    place = models.CharField(max_length=50)
    date = models.DateField()
    price = models.PositiveIntegerField()
    ticket_count = models.IntegerField()
    
    def __str__(self):
        return f"{self.country} - {self.city} - {self.place} - {self.date} - {self.price} - {self.ticket_count}"
    
    
    
    