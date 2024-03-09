from django.urls import path
from .views import *

urlpatterns = [
    path('admin/login', checkIfAdmin, name='loginForm'),
    # path('admin/checkIfAdmin', checkIfAdmin, name='checkIfAdmin'),
]
