from django.shortcuts import render
from .models import RendezVous
# Create your views here.


def liste_rendezvous(request):
    rendezvous = RendezVous.objects.all()
    return render(request, 'index.html', {'rendezvous': RendezVous})