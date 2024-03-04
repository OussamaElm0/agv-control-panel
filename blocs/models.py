from django.db import models

# Create your models here.
class Bloc(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom