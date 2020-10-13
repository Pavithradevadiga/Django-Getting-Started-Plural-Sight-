from django.db import models
from datetime import time

# Create your models here.

class Room(models.Model):
    Name = models.CharField(max_length=20)
    Floor = models.IntegerField()
    No = models.IntegerField()

    def __str__(self):
        return f"Meeting will be held in the Floor:{self.Floor} RoomNo: {self.No} Name:{self.Name}"          
 

class Meeeting(models.Model):
    Title = models.CharField(max_length=20)
    Date = models.DateField()
    Time = models.TimeField(default=time(9))
    Duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Title} will be held on {self.Date} at {self.Time} for {self.Duration} hour/s"    


