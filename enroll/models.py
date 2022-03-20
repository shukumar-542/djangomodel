from django.db import models

# Create your models here.


class Students(models.Model):
    stid = models.IntegerField()
    stname = models.CharField(max_length=70)
    stemail = models.EmailField(max_length=70)
    stpass = models.CharField(max_length=70)

    
#     def __str__(self):
#           return self.stname
