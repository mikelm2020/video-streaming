from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from django.shortcuts import get_object_or_404

from apps.video.models import Video
from apps.video.api.video_serializers import (
    VideoSerializer,
    FilmGenreSerializer,
    ClassificationSerializer,
    CountrySerializer,
    ProviderSerializer,
    SeasonSerializer,
    SeasonRegisterSerializer,
)
from apps.core.models import *


class VideoViewSet(viewsets.GenericViewSet):
    serializer_class = VideoSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return Video.objects.filter(state=True)
        else:
            return Video.objects.filter(id=pk, state=True).first()

    def get_object(self, pk):
        return get_object_or_404(Video, pk=pk)

    def list(self, request):
        video_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(video_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            if serializer.data["video_type"] == "S":
                data_season = {
                    "video": serializer.data["id"],
                    "chapters": 6,
                    "number_season": 1,
                }
            else:
                data_season = {
                    "video": serializer.data["id"],
                    "chapters": 0,
                    "number_season": 0,
                }
            
            data_season = SeasonRegisterSerializer(data=data_season)

            if data_season.is_valid():
                data_season.save()

            return Response(
                {"message": "Video registrado correctamente"},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"message": "Hay errores en el registro", "error": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def retrieve(self, request, pk=None):
        video = self.get_object(pk)
        video_serializer = self.serializer_class(video)
        return Response(video_serializer.data)

    def update(self, request, pk=None):
        video = self.get_object(pk)
        video_serializer = self.serializer_class(video, data=request.data)
        if video_serializer.is_valid():
            video_serializer.save()
            return Response(
                {"message": "Video actualizado correctamente"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "message": "Hay errores en la actualización",
                "error": video_serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def destroy(self, request, pk=None):
        video_destroy = self.serializer_class.Meta.model.objects.filter(id=pk).update(
            state=False
        )
        if video_destroy == 1:
            return Response(
                {"message": "Video eliminado correctamente!"}, status=status.HTTP_200_OK
            )
        return Response(
            {"message": "No existe el video que desea eliminar"},
            status=status.HTTP_404_NOT_FOUND,
        )

    def partial_update(self, request, pk=None):
        """Update with data of the serie's season"""

        video = self.get_object(pk)
        video_serializer = SeasonSerializer(video, data=request.data, partial=True)
        if video_serializer.is_valid():
            video_serializer.save()
            return Response(
                {
                    "message": "Video actualizado correctamente con los datos de la temporada"
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "message": "Hay errores en la actualización",
                "error": video_serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    @action(methods=["get"], detail=False)
    def get_film_genre(self, request):

        data = FilmGenre.objects.filter(state=True).order_by("id")
        data = FilmGenreSerializer(data, many=True).data
        return Response(data)

    @action(methods=["get"], detail=False)
    def get_classification(self, request):

        data = Classification.objects.filter(state=True).order_by("id")
        data = ClassificationSerializer(data, many=True).data
        return Response(data)

    @action(methods=["get"], detail=False)
    def get_country(self, request):

        data = Country.objects.filter(state=True).order_by("id")
        data = CountrySerializer(data, many=True).data
        return Response(data)

    @action(methods=["get"], detail=False)
    def get_provider(self, request):

        data = Provider.objects.filter(state=True).order_by("id")
        data = ProviderSerializer(data, many=True).data
        return Response(data)
