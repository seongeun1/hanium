from django.db import models

# Create your models here.
class TourType(models.Model):
    tour_id = models.IntegerField()
    name = models.CharField(max_length=100)
    abbr = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'TOUR_TYPE'

class Travelholic(models.Model):
    content = models.CharField(max_length=5000)
    posted_date = models.CharField(max_length=50)
    like = models.CharField(max_length=50)
    place = models.CharField(max_length=500)
    tags = models.CharField(max_length=500)
    crawled_date = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'TravelHolic'
