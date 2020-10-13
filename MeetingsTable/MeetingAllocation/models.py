from django.db import models
from datetime import time

# Create your models here.
class Meeeting(models.Model):
    Title = models.CharField(max_length=20)
    Date = models.DateField()
    Time = models.TimeField(default=time(9))
    Duration = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.Title} will be held on {self.Date} at {self.Time} for {self.Duration} hour/s"    

class Room(models.Model):
    Name = models.CharField(max_length=20)
    Floor = models.IntegerField()
    No = models.IntegerField()

    def __str__(self):
        return f"Meeting is being held in the floor {self.Floor} :{self.no} {self.Name}"     