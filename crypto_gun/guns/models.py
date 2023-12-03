from django.db import models

# Create your models here.

class Gun(models.Model):

    serial_number = models.CharField(max_length=50, unique=True, null=False, blank=False)
    type = models.CharField(max_length=20, blank=False, null=False)
