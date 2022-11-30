from apps.base.pagination import ExtendedPagination
from apps.playlist.api.playlist_serializers import (
    PlaylistListSerializer,
    PlaylistSerializer,
    PlaylistVideoSerializer,
    PlaylistVideoUpdateSerializer,
)
from apps.playlist.models import Playlist
from django.shortcuts import get_object_or_404
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiParameter,
    extend_schema,
    extend_schema_view,
)
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication


class PlaylistViewSet(viewsets.GenericViewSet):

    serializer_class = PlaylistSerializer
    list_serializer_class = PlaylistListSerializer
    pagination_class = ExtendedPagination

    def get_queryset(self, pk=None):
        if pk is None:
            return Playlist.objects.filter(state=True, user=self.request.user)
        else:
            return Playlist.objects.filter(
                id=pk, state=True, user=self.request.user
            ).first()

    def get_object(self, pk):
        return get_object_or_404(Playlist, pk=pk)

    @extend_schema(request=PlaylistListSerializer)
    def list(self, request, *args, **kwargs):
        """
        Get a collection of Playlists
        """
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.list_serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.list_serializer_class(queryset, many=True)
        return Response(serializer.data)

    def format_data(self, data):
        # Return data with the user
        JWT_authenticator = JWTAuthentication()
        # Decode token
        user, _ = JWT_authenticator.authenticate(self.request)
        data["user"] = user.id
        return data

    @extend_schema(
        request=PlaylistSerializer,
        responses={201: None},
        examples=[
            OpenApiExample(
                "Example 1",
                description="Request to playlist",
                value={"user": 0, "provider": 0, "video": [0]},
            ),
        ],
    )
    def create(self, request):
        """
        Create a Playlist
        """
        data = self.format_data(data=request.data)
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():

            serializer.save()

            return Response(
                {"message": "Playlist registrada correctamente"},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"message": "Hay errores en el registro", "error": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="id", type=OpenApiTypes.INT, location=OpenApiParameter.PATH
            ),
        ],
    )
    def retrieve(self, request, pk=None):
        """
        Get a Playlist
        """
        playlist = self.get_object(pk)
        playlist_serializer = self.list_serializer_class(playlist)
        return Response(playlist_serializer.data)

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="id", type=OpenApiTypes.INT, location=OpenApiParameter.PATH
            ),
        ],
    )
    def destroy(self, request, pk=None):
        """
        Delete a Playlist in logical mode
        """
        playlist_destroy = self.serializer_class.Meta.model.objects.filter(
            id=pk
        ).update(state=False)
        if playlist_destroy == 1:
            return Response(
                {"message": "Playlist eliminada correctamente!"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"message": "No existe la playlist que desea eliminar"},
            status=status.HTTP_404_NOT_FOUND,
        )


@extend_schema_view(
    list=extend_schema(operation_id="list"),
    retrieve=extend_schema(operation_id="retrieve"),
    partial_update=extend_schema(operation_id="partial_update"),
)
class PlaylistVideoViewSet(viewsets.GenericViewSet):
    serializer_class = PlaylistVideoSerializer
    pagination_class = ExtendedPagination

    def get_queryset(self, pk=None):
        if pk is None:
            return Playlist.video.through.objects.filter()
        else:
            return Playlist.video.through.objects.filter(id=pk).first()

    def get_object(self, pk):
        return get_object_or_404(Playlist.video.through, season_id=pk)

    def list(self, request, *args, **kwargs):
        """
        Get a collection of Playlists' videos
        """
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Get a Playlist's video
        """
        video_in_playlist = self.get_object(pk)
        video_in_playlist_serializer = self.serializer_class(video_in_playlist)
        return Response(video_in_playlist_serializer.data)

    @extend_schema(
        request=PlaylistVideoUpdateSerializer,
        responses=PlaylistVideoUpdateSerializer,
    )
    def partial_update(self, request, pk=None):
        """
        Update the serie how viewed
        """
        season = self.get_object(pk)
        season_serializer = PlaylistVideoUpdateSerializer(
            season, data=request.data, partial=True
        )
        if season_serializer.is_valid():
            season_serializer.save()
            return Response(
                {"message": "La temporada ha sido marcada como vista correctamente!"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "message": "Hay errores en la actualización",
                "error": season_serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
