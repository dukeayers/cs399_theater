from django.db import models


class Movie(models.Model):
    movie_title = models.CharField(max_length = 30)
    movie_time = models.CharField(max_length = 30)
    movie_day = models.DateField()

class Info(models.Model):
    info_rating = models.CharField(max_length = 3)
    info_title = models.CharField(max_length = 200)
    info_description = models.CharField(max_length = 400)
    info_thumbnail = models.CharField(max_length = 400)

class Store(models.Model):
    store_item = models.CharField(max_length = 100)
    store_description = models.CharField(max_length = 300)
    store_price = models.CharField(max_length = 40)

