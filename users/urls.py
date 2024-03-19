from django.urls import path
from .views import checkIfAdmin, dashboard, adminLogout, commande, sendCommand, updateCommande

urlpatterns = [
    path('admin/login', checkIfAdmin, name='loginForm'),
    path('dashboard', dashboard, name='adminIndex'),
    path('admin/logout', adminLogout, name="adminLogout"),
    path('',commande, name="home"),
    path('sendCommand',sendCommand, name='sendCommand'),
    path('update-status/<id>', updateCommande, name='update_status'),
]
