from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_rendezvous, name='liste_rendezvous'),
]