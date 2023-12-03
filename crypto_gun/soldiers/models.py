from django.db import models
from guns.models import Gun
# Create your models here.

class Soldier(models.Model):

    first_name = models.CharField(max_length=50, null=False, blank=False)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    national_id = models.CharField(max_length=20, null=False, blank=False, unique=True)


class SoldierGun(models.Model):

    soldier = models.ForeignKey(Soldier, on_delete=models.CASCADE)
    gun = models.ForeignKey(Gun, on_delete=models.CASCADE)


class SoldierWallet(models.Model):

    soldier = models.ForeignKey(Soldier, on_delete=models.CASCADE)
    wallet_address = models.CharField(max_length=200, null=False)
    private_key = models.BinaryField(null=False)