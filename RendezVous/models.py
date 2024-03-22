from django.db import models

# Create your models here.
class RendezVous(models.Model):
    nom = models.CharField(max_length=100)
    date = models.DateField()
    heure = models.TimeField()
    description = models.TextField()

    def __str__(self):
        return self.nom