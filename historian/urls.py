from django.urls import path
from . import views
from .views import PersonajeDetailView, HechoDetailView

urlpatterns = [
    path('verhecho/', views.hecho_historico, name='verhecho'),
    path('figuras/', views.figuras, name='figuras'),
    path('detalles/<int:pk>', PersonajeDetailView.as_view(), name='detalles'),
    path('hechodetail/<int:pk>', HechoDetailView.as_view(), name='hechodetail'),
    path('buscar/', views.buscar, name='buscar'),
    path('aviso/', views.alerta, name='aviso'),
]
