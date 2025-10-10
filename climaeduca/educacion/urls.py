from django.urls import path
from . import views

urlpatterns = [
    path('prueba/', views.prueba_firebase, name='prueba_firebase'),
]