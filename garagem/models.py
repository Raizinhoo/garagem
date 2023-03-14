from django.db import models

class Marca(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Categoria(models.Model):
    descricão = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
