from django.urls import path

from . import views

urlpatterns = [
    path('vermelha/', views.vermelha, name='vermelha'),
    path('verde/', views.verde, name='verde'),
    path('azul/', views.azul, name='azul'),
    path('amarela/', views.amarela, name='amarela'),
]
