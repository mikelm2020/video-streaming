from apps.core.models import *
from django.contrib import admin


@admin.register(FilmGenre)
class FilmGenreAdmin(admin.ModelAdmin):

    list_display = ("id", "film_genre")
    list_filter = ("film_genre",)
    search_fields = ("film_genre",)
    ordering = ("id", "film_genre")


@admin.register(Classification)
class ClassificationAdmin(admin.ModelAdmin):

    list_display = ("id", "age_rating")
    list_filter = ("age_rating",)
    search_fields = ("age_rating",)
    ordering = ("id", "age_rating")


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):

    list_display = ("id", "country")
    list_filter = ("country",)
    search_fields = ("country",)
    ordering = ("id", "country")


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):

    list_display = ("id", "provider")
    list_filter = ("provider",)
    search_fields = ("provider",)
    ordering = ("id", "provider")
