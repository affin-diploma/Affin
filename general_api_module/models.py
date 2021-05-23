from django.db import models

# Create your models here.


class DataSource(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    api = models.CharField(max_length=2048)
