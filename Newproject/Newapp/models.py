from django.db import models

# Create your models here.
class Employee(models.Model):
    ename=models.CharField(max_length=20)
    eid=models.IntegerField()
    eexp=models.FloatField()
    esal=models.FloatField()
