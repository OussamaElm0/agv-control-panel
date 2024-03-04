from django.contrib import admin
from .models import Commande

# Register your models here.
@admin.register(Commande)
class CommandModel(admin.ModelAdmin):
    list_display = (
        'id',
        'agv',
        'bloc',
        'date',
        'time',
    )