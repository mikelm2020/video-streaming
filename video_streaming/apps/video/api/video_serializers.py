from rest_framework import serializers
from apps.video.models import Video
from apps.core.models import *
from apps.core.api.core_serializers import *
from apps.season.models import Season


class VideoSerializer(serializers.ModelSerializer):
    class Meta:

        model = Video

        exclude = (
            "state",
            "created_date",
            "modified_date",
            "deleted_date",
        )

    def validate(self, data):
        if data["video_type"] == "M":
            if data["duration"] == 0:
                raise serializers.ValidationError(
                    {"duration": "La duración de una pélicula no puede ser 0"}
                )
        return data


class SeasonRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ("video", "chapters", "number_season")

    def save(self):

        new_season = Season.objects.create(**self.validated_data)
        return new_season


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
        fields = ("id", "country")


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ("id", "provider")


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ("chapters", "number_season")
