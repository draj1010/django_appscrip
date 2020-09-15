from django.db import models
from datetime import datetime

#model for main game
class Game(models.Model):
    name = models.CharField(max_length=100)
    que_one = models.CharField(max_length=100)
    que_two = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now, blank=True)

    #to retrieve default title for model
    def __str__(self):
        return self.name
