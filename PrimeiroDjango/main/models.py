from django.db import models
from datetime import datetime as dt

# Create your models here.

class MeusfilmesFavoritos(models.Model):
    # Aqui definimos as colunas que teremos em nosso banco de dados
    titulo = models.CharField(max_length=50)
    resumo = models.TextField()
    data = models.DateTimeField("Publicado em", default=dt.now())

    def __str__(self):
        return self.titulo
