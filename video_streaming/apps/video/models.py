from django.db import models

from apps.core.models import FilmGenre, Classification, Country, Provider
from apps.base.models import BaseModel


class Video(BaseModel):
    """Model definition for the streaming's material."""

    VIDEO_TYPE_CHOICES = (
        ("S", "Serie"),
        ("M", "Pelicula"),
        ("D", "Documental"),
        ("R", "Reality"),
    )

    name = models.CharField("Nombre", max_length=200)
    num_year = models.IntegerField(verbose_name="Año")
    video_type = models.CharField("Tipo", max_length=1, choices=VIDEO_TYPE_CHOICES)
    film_genre = models.ManyToManyField(
        FilmGenre, verbose_name="Genero Cinematográfico"
    )
    classification = models.ForeignKey(
        Classification, on_delete=models.CASCADE, verbose_name="Clasificación"
    )
    country = models.ManyToManyField(Country, verbose_name="Pais")
    provider = models.ManyToManyField(Provider, verbose_name="Proveedor")
    duration = models.IntegerField(verbose_name="Duración", blank=True)
    chapters = models.SmallIntegerField(verbose_name="Capitulos", default=0)
    number_season = models.SmallIntegerField(verbose_name="Temporada", default=0)
    viewed = models.BooleanField(verbose_name="Vista", default=False)


    class Meta:

        verbose_name = "Video"
        verbose_name_plural = "Videos"

    def __str__(self):
        return self.name

    