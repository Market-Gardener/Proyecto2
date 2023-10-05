from django.urls import path
from AppIsaac import views

urlpatterns = [
    path('inicio/', views.inicio, name="Inicio"),
    path('pisinas/', views.pisina, name="Pisinas"),
    path('items/', views.items, name="Items"),
    path('usuario/', views.users, name="Users"),
    #path('form/', views.pisinaForm, name="PisinaForm"),
    path('bPisinas/', views.busquedaPisina, name="BusquedaPisina"),
    path('buscar/', views.buscar),
]
