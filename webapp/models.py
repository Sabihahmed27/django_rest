from django.db import models

# Create your models here.


class employees(models.Model):
    firstname = models.CharField(max_length=10,blank=False)
    lastname = models.CharField(max_length=10,blank=False)
    emd_id = models.IntegerField(blank=False)

    def __str__(self):
        return self.firstname

