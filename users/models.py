from django.db import models
from blocs.models import Bloc

# Create your models here.
class Poste(models.Model):
    mac_address = models.CharField(max_length=17, unique=True)
    bloc = models.ForeignKey(Bloc, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.mac_address