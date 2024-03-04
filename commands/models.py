from django.db import models
from agv.models import Agv
from blocs.models import Bloc

# Create your models here.
class Commande(models.Model):
    agv = models.ForeignKey(Agv, on_delete=models.CASCADE)
    bloc = models.ForeignKey(Bloc, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f'Agv: {self.agv.nom} to Bloc: {self.bloc.nom}'