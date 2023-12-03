# Generated by Django 4.2.7 on 2023-12-03 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soldiers', '0003_rename_nationla_id_soldier_national_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoldierWallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet', models.CharField(max_length=200)),
                ('soldier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soldiers.soldier')),
            ],
        ),
    ]
