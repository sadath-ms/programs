from django.db import models

from django.urls import reverse

# Create your models here.

class NameModel(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    location=models.CharField(max_length=30)


    def get_absolute_url(self):
        return reverse('first_project:details',kwargs={'pk':self.pk})



