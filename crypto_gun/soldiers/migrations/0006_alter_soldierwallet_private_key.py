# Generated by Django 4.2.7 on 2023-12-03 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soldiers', '0005_rename_wallet_soldierwallet_wallet_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soldierwallet',
            name='private_key',
            field=models.BinaryField(),
        ),
    ]