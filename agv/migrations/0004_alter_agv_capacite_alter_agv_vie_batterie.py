# Generated by Django 5.0 on 2024-03-06 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agv', '0003_alter_agv_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agv',
            name='capacite',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='agv',
            name='vie_batterie',
            field=models.PositiveIntegerField(),
        ),
    ]