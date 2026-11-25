from django.db import models

class Avaliação(models.Model):

    estrelas = models.DecimalField(
        max_digits=1
        decimal_places=1
        null=False
        blank=False
    )

    comentario = models.Charfield(
        max_Length=255
        null=False
        blank=True
    )

    objetos = models.Manager()