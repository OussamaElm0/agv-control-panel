# Generated by Django 4.1.13 on 2024-03-12 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commandes', '0002_commande_confirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='date',
            field=models.DateField(default='2024-03-12'),
        ),
        migrations.AddField(
            model_name='commande',
            name='time',
            field=models.TimeField(default='11:23:02'),
        ),
    ]
