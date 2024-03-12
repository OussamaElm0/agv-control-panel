from django.shortcuts import render
from agv.models import Agv
from blocs.models import Bloc
from .models import Commande

# Create your views here.
def sendCommand(agvId, blocID):
    agv = Agv.objects.get(pk=agvId)
    bloc = Bloc.objects.get(pk=blocID)
    command = Commande(id_agv=agv, id_bloc= bloc)
    command.save()