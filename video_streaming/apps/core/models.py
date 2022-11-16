from apps.base.models import BaseModel
from django.db import models


class FilmGenre(BaseModel):
    """Model definition for classification of the film."""

    film_genre = models.CharField("Genero cinematográfico", max_length=50)

    class Meta:

        verbose_name = "Genero"
        verbose_name_plural = "Generos"

    def __str__(self):
        return self.film_genre


class Classification(BaseModel):
    """Model definition for classification recommended for age."""

    age_rating = models.CharField("Clasificación", max_length=5)

    class Meta:

        verbose_name = "Clasificación"
        verbose_name_plural = "Clasificaciones"

    def __str__(self):
        return self.age_rating


class Country(BaseModel):
    """Model definition for Countries exhibiting the film."""

    country = models.CharField("País", max_length=50)
    iso_code = models.CharField("Codigo ISO", max_length=3)

    class Meta:

        verbose_name = "País"
        verbose_name_plural = "Paises"

    def __str__(self):
        return f"{self.iso_code} - {self.country}"


class Provider(BaseModel):
    """Model definition for Provider of streaming's services."""

    provider = models.CharField("Proveedor", max_length=15)

    class Meta:

        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return self.provider
