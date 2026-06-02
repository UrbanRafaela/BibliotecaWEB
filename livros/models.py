from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    ano = models.IntegerField()
    quantidade = models.IntegerField()
    capa = models.ImageField(upload_to='capas/', blank=True, null=True)

    def __str__(self):
        return self.titulo