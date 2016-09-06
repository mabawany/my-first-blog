from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Set(models.Model):
    title = models.TextField()
    timestamp = models.DateTimeField()
    phrase = models.TextField()
    relevance  = models.FloatField()

def publish(self):
    self.save()


def __str__(self):
    return self.title
