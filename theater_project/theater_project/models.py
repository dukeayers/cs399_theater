from django.db import models

class Info(models.Model):
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 400)
    rating = models.CharField(max_length = 400)
    thumbnail = models.CharField(max_length = 400)
    duration = models.CharField(max_length = 400)

class Movie(models.Model):
    title = models.CharField(max_length = 200)
    time = models.CharField(max_length = 30)

class Store(models.Model):
    item = models.CharField(max_length = 100)
    description = models.CharField(max_length = 300)
    price = models.CharField(max_length = 40)
    thumbnail = models.CharField(max_length = 400)
    source = models.CharField(max_length = 400)

class Event(models.Model):
    title = models.CharField(max_length = 100)
    date = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    descr = models.CharField(max_length=200)