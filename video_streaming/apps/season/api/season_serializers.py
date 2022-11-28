from apps.season.models import Season
from apps.video.api.video_serializers import VideoSerializer
from rest_framework import serializers


class SeasonSerializer(serializers.ModelSerializer):
    video = VideoSerializer()

    class Meta:
        model = Season
        fields = (
            "id",
            "video",
            "chapters",
            "number_season",
        )

    def validate_chapters(self, value):
        if value == 0:
            raise serializers.ValidationError(
                {"Falta registrar el número de capitulos de la temporada"}
            )

    def validate_number_season(self, value):
        if value == 0:
            raise serializers.ValidationError(
                {"Falta registrar el número de temporada"}
            )


class SeasonUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = (
            "chapters",
            "number_season",
        )


class SeasonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ("video", "chapters", "number_season")

    def validate(self, data):
        from django.db.models import Max

        if data["video"].video_type != "S":
            raise serializers.ValidationError(
                {"video": "El id del video no pertenece a una serie!"}
            )
        else:
            actual_season = Season.objects.filter(
                state=True, video=data["video"].id
            ).aggregate(Max("number_season"))

            if data["number_season"] - actual_season.get("number_season__max") != 1:
                raise serializers.ValidationError(
                    {"number_season": "Número de temporada inválido!"}
                )
        return data
