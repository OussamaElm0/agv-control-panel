from django.db import models

# Create your models here.
class Agv(models.Model):
    statusOptions = (
        ('Inactive', 'Inactive'),
        ('Porter une charge', 'Porter une charge'),
        ('Mise en charge', 'Mise en charge')
    )

    nom = models.CharField(max_length=100)
    capacite = models.IntegerField()
    vie_batterie = models.IntegerField()
    status = models.CharField(max_length=50,choices=statusOptions)

    def __str__(self):
        return self.nom