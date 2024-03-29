from django.db import models

# Create your models here.
class Agv(models.Model):
    statusOptions = (
        ('IN', 'Inactive'),
        ('PC', 'Porter une charge'),
        ('MC', 'Mise en charge')
    )

    nom = models.CharField(max_length=100)
    capacite = models.PositiveIntegerField()
    vie_batterie = models.PositiveIntegerField()
    status = models.CharField(max_length=50,choices=statusOptions)

    def __str__(self):
        return self.nom