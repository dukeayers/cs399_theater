from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length = 30)
    time = models.CharField(max_length = 30)

class Info(models.Model):
    rating = models.CharField(max_length = 3)
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 400)
    thumbnail = models.CharField(max_length = 400)

class Store(models.Model):
    item = models.CharField(max_length = 100)
    description = models.CharField(max_length = 300)
    price = models.CharField(max_length = 40)
