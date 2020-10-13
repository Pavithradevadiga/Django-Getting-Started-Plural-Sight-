from django.db import models

# Create your models here.
class Meeeting(models.Model):
    Title = models.CharField(max_length=20)
    Date = models.DateField()