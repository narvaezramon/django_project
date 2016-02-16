from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Usuario(models.Model):
    name = models.CharField(max_length=250, default=False)
    go = models.IntegerField()
    password = models.CharField(max_length=250, default=False)
