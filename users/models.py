from django.db import models
from agv.models import Agv
from blocs.models import Bloc

# Create your models here.
class Utilisateur(models.Model):
    def sendAgv(self,agv: Agv, bloc: Bloc):
        pass

    class Meta:
        abstract = True

class Admin(Utilisateur):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.username

class Poste(Utilisateur):
    id = models.AutoField(primary_key=True)
    ip_address = models.GenericIPAddressField()
    bloc = models.ForeignKey(Bloc, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.ip_address