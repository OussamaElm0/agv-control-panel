from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display= (
        'id',
        'id_agv',
        'id_bloc',
        'date',
        'time',
        'confirmed'
    )