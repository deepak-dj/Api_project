from django.db import models

class employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=200)
    esal = models.IntegerField()

