from django.contrib.admin import register, ModelAdmin
from .models import *

# Register your models here.
@register(Poste)
class PosteAdmin(ModelAdmin):
    list_display = (
        'ip_address',
        'bloc'
    )