from django.shortcuts import render
from agv.models import Agv
from blocs.models import Bloc
from .models import Commande
import datetime as dt

# Create your views here.
def sendCommand(agvId, blocID):
    agv = Agv.objects.get(pk=agvId)
    bloc = Bloc.objects.get(pk=blocID)
    date = dt.datetime.now().strftime("%Y-%m-%d")
    time = dt.datetime.now().strftime("%H:%M")

    command = Commande(id_agv=agv, id_bloc= bloc, date= date, time= time)
    command.save()