from django.urls import path
from AppEntrega import views
#from Entrega.AppEntrega.models import Profesional

urlpatterns = [
    
    path('', views.inicio, name="Inicio"),
    path('Lista de Precios',views.listadeprecios, name="Lista de Precios"),
    path('Cliente', views.cliente, name="Cliente"),
    path('Profesional',views.profesional, name ="Profesional" ),
    path('Turnos', views.turnos, name="Turnos"),
    path('Clienteformulario', views.cliente, name="ClienteFormulario"),
    path('Lista de Precioformulario', views.listadeprecios, name="Lista de PreciosFormulario"),
    path('Profesionalformulario', views.profesional, name="ProfesionalFormulario"),
    path('Turnosformulario', views.turnos, name="TuenosFormulario"),
    path('buscar/', views.buscar),
    
    
    
    
    
]


