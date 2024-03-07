from django.urls import path
from .views import *

urlpatterns = [
    path('admin/login', adminLogin, name='adminLogin'),
]
