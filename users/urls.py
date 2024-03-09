from django.urls import path
from .views import *

urlpatterns = [
    path('admin/login', loginForm, name='loginForm'),
    path('admin/checkIfAdmin', checkIfAdmin, name='checkIfAdmin'),
]
