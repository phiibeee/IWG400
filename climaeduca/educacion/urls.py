from django.urls import path
from . import views

urlpatterns = [
    path('prueba/', views.prueba, name='prueba_firebase'),
    path('registro/', views.registro_user, name = 'registro_user'),
]