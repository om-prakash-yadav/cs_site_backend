import datetime
from django.db import models

# Create your models here.
class Faculty(models.Model):
  name = models.CharField(max_length=100)
  image=models.ImageField(upload_to='images/faculty')
  email = models.EmailField(unique=True)
  phoneno=models.IntegerField(default=0)
  post = models.CharField(max_length=100)
  interest_area_1 = models.CharField(max_length=100)
  interest_area_2 = models.CharField(max_length=100)
  joined_year = models.IntegerField(default=0)
  def __str__(self):
         return self.name

class Staff(models.Model):
  name = models.CharField(max_length=100)
  image=models.ImageField(upload_to='images/staff')
  email = models.EmailField(unique=True)
  phoneno=models.IntegerField(default=0)
  post = models.CharField(max_length=100)
  interest_area_1 = models.CharField(max_length=100)
  interest_area_2 = models.CharField(max_length=100)
  joined_year = models.IntegerField(default=0)
  def __str__(self):
         return self.name

class Feed(models.Model):
  name = models.CharField(max_length=100)
  link = models.CharField(max_length=5000,blank=True,default=" ")
  date = models.DateField(default=0)
  def __str__(self):
         return self.name



class Event(models.Model):
  CHOICES = [
        ('upcoming', 'upcoming'),
        ('past', 'past'),
    ]
  EventName = models.CharField(max_length=100)
  Date = models.DateTimeField()
  Link = models.CharField(max_length=5000,blank=True,default=" ")
  EventType = models.CharField(max_length=10, choices=CHOICES)
  
  def __str__(self):
         return self.EventName


class gallery(models.Model):
  Image=models.ImageField(upload_to='images/gallery')

