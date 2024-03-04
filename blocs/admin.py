from django.contrib import admin
from .models import Bloc

# Register your models here.
@admin.register(Bloc)
class BlocModel(admin.ModelAdmin):
    list_display = (
        'id',
        'nom',
    )