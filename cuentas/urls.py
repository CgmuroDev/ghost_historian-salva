# cuentas/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('crearcuenta/', registro, name='crearcuenta'),
    path('salir/', salir, name='salir'),
    path('ver/<int:pk>/', ver, name='ver'),
    path('eliminar/<int:pk>/', eliminar, name='eliminar'),
    path('editar/<int:pk>/', editar, name='editar'),
    path('login/', entrar, name='login'),
]
