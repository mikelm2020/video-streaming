from apps.playlist.models import Playlist, PlaylistVideo
from apps.season.api.season_serializers import SeasonSerializer
from apps.users.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "name",
            "last_name",
        )


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = (
            "user",
            "provider",
            "video",
        )


class PlaylistListSerializer(serializers.Serializer):
    user = UserSerializer()
    video = SeasonSerializer(many=True)


class PlaylistVideoSerializer(serializers.ModelSerializer):
    season_id = SeasonSerializer()

    class Meta:
        model = PlaylistVideo
        fields = (
            "playlist_id",
            "season_id",
            "viewed",
        )


class PlaylistVideoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaylistVideo
        fields = ("viewed",)

    def to_representation(self, instance):
        return {"viewed" : instance["viewed"]}