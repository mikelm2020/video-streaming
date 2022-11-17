from rest_framework import serializers
from apps.playlist.models import Playlist
from apps.video.models import Video
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "name", "last_name")


class VideoSerializer(serializers.ModelSerializer):
    # viewed = serializers.BooleanField()

    class Meta:
        model = Video
        fields = (
            "id",
            "name",
            "video_type",
            "duration",
            "chapters",
            "number_season",
            "viewed",
        )


# class ViewedVideoSerializer(serializers.ModelSerializer):
#     viewed = serializers.BooleanField()

#     class Meta:
#         model = Video
#         fields = ("id",)

#     def to_representation(self, instance):
#         return {
#             "pk": instance["pk"],
#             "viewed": instance["viewed"]
#         }


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        exclude = (
            "state",
            "created_date",
            "modified_date",
            "deleted_date",
        )


class PlaylistVideoSerializer(serializers.Serializer):
    user = UserSerializer()
    video = VideoSerializer(many=True, read_only=True)
    
   


