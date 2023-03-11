from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class StreamingPlateform(models.Model):
    name=models.CharField(max_length=20)
    about=models.CharField(max_length=200)
    website=models.URLField(max_length=200)

    def __str__(self):
        return self.name

class WatchList(models.Model):
    name=models.CharField(max_length=20)
    storyline=models.CharField(max_length=500)
    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    plateform=models.ForeignKey(StreamingPlateform, on_delete=models.CASCADE,related_name='WatchList')
    avg_rating=models.FloatField(default=0)
    number_rating=models.IntegerField(default=0)
    
    def __str__(self):
        return self.name


class Reviews(models.Model):
    review_user=models.ForeignKey(User, on_delete=models.CASCADE)
    rating=models.IntegerField()
    comment=models.CharField(max_length=200,null=True)
    watchlist=models.ForeignKey(WatchList, on_delete=models.CASCADE,related_name='movieReview')
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rating)+' | '+self.watchlist.name