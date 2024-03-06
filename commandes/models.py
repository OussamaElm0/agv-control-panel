from django.db import models
from agv.models import Agv
from blocs.models import Bloc
import datetime as dt
from django.utils import timezone


# Create your models here.
class Commande(models.Model):
    id_agv = models.ForeignKey(Agv, on_delete=models.CASCADE)
    id_bloc = models.ForeignKey(Bloc, on_delete=models.CASCADE)
    date = dt.datetime.now().strftime("%Y-%m-%d")
    time = dt.datetime.now().strftime("%H:%M:%S")
    confirmed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'Agv: {self.id_agv} to Bloc: {self.id_bloc}'
