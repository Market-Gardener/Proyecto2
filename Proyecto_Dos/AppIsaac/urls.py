from django.urls import path
from AppIsaac import views

urlpatterns = [
    path('/', views.inicio),
    path('pisinas/', views.pisina),
    path('items/', views.items),
    path('usuario/', views.users),
]
