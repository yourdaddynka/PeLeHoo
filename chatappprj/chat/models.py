from django.db import models
from datetime import datetime

class Room(models.Model):
    name = models.CharField(max_length=1000)

class Message(models.Model):
    value = models.CharField(max_length=300)
    date = models.DateTimeField(default=datetime.now, blank=True)
    room = models.CharField(max_length=300)
    user = models.CharField(max_length=300)