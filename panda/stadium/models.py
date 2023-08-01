from django.db import models
from django.urls import reverse



class Stadium(models.Model):
    # id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    abbr_name = models.CharField(max_length=100)
    en_name = models.CharField(max_length=255)
    club_name = models.CharField(max_length=255)
    league = models.CharField(max_length=100)
    num_people = models.IntegerField(null=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('stadium:details', kwargs={'pk': self.pk})