from django.contrib import admin
from .models import Agv

# Register your models here.
@admin.register(Agv)
class AgvModel(admin.ModelAdmin):
    list_display = (
        'id',
        'nom',
        'capacite',
        'vie_batterie',
        'status'
    )
