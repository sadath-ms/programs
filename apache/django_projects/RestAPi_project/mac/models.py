from django.db import models

# Create your models here.
class emp(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    age=models.IntegerField(default=True)

    def __str__(self):
        return self.first_name+'--'+self.last_name+'--'+self.gender+'--'+str(self.age)



