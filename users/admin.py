from django.contrib.admin import register, ModelAdmin
from .models import *
# Register your models here.

@register(Admin)
class AdminAdmin(ModelAdmin):
    list_display = (
        'username',
        'password'
    )

@register(Poste)
class PosteAdmin(ModelAdmin):
    list_display = (
        'ip_address',
        'bloc'
    )