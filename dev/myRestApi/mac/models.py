from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    location=models.CharField(max_length=100)