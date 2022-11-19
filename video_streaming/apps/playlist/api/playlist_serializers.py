from rest_framework import serializers
from apps.playlist.models import Playlist
from apps.users.models import User
from apps.season.api.season_serializers import SeasonSerializer


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


class PlaylistVideoSerializer(serializers.Serializer):
    user = UserSerializer()
    video = SeasonSerializer(many=True)
