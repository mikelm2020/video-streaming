from rest_framework import serializers
from apps.season.models import Season
from apps.video.api.video_serializers import VideoSerializer


class SeasonSerializer(serializers.ModelSerializer):
    video = VideoSerializer()

    class Meta:
        model = Season
        fields = (
            "id",
            "video",
            "chapters",
            "number_season",
            "viewed",
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
