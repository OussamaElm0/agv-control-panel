from django.urls import path
from .views import *

urlpatterns = [
    path('admin/login', adminLogin, name='adminLogin'),
    path('admin/home', test, name='test'),
]
