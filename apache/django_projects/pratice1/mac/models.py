from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=30)
    age=models.CharField(max_length=50)
    location=models.CharField(max_length=20)

    def __str__(self):
        return self.name+' - '+self.gender+' - '+self.age+' - '+self.location



