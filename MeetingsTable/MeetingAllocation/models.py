from django.db import models
from datetime import time

# Create your models here.
class Meeeting(models.Model):
    Title = models.CharField(max_length=20)
    Date = models.DateField()
    Time = models.TimeField(default=time(9))
    Duration = models.IntegerField(default=1)