from django.db import models

class Departures(models.Model):
    Departures = []

class Destination(models.Model):
    Destinations = []

class Login(models.Model):
    UserName = models.CharField(max_length=150)
    Password = models.CharField(max_length=150)
    login_attemp_time = models.TimeField()

class User(models.Model):
    depart = Departures()
    Destination = Destination()
    UserName = models.CharField(max_length=200)
    Password = models.CharField(max_length=150)
    Lat = models.IntegerField()
    Lang = models.IntegerField()
    SiteVisit = models.IntegerField()
    RouteRequested = models.CharField(choices=depart.Departures,max_length=150)
    RouteRequestCount = models.IntegerField()
    LastVist = models.TimeField(blank=True)
