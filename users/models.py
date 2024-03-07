from django.db import models
from agv.models import Agv
from blocs.models import Bloc
from django.contrib.auth.models import User

# Create your models here.
class Poste(models.Model):
    ip_address = models.GenericIPAddressField()
    bloc = models.ForeignKey(Bloc, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.ip_address