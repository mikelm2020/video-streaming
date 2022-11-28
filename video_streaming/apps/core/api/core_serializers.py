from apps.core.models import *
from rest_framework import serializers


class FilmGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmGenre
        fields = ("id", "film_genre")


class ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = ("id", "age_rating")


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("id", "country", "iso_code")


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ("id", "provider")
