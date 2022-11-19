from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from django.shortcuts import get_object_or_404

from apps.season.models import Season
from apps.season.api.season_serializers import (
    SeasonSerializer,
    SeasonUpdateSerializer,
)
from apps.core.models import *


class SeasonViewSet(viewsets.GenericViewSet):
    serializer_class = SeasonSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return Season.objects.filter(state=True, video__video_type="S")
        else:
            return Season.objects.filter(id=pk, state=True).first()

    def get_object(self, pk):
        return get_object_or_404(Season, pk=pk)

    def list(self, request):
        season_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(season_serializer.data, status=status.HTTP_200_OK)

    # def create(self, request):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         if serializer.data["season_type"] == "S":
    #             data_season = {
    #                 "season": serializer.data["id"],
    #                 "chapters": 6,
    #                 "number_season": 1,
    #             }
    #         else:
    #             data_season = {
    #                 "season": serializer.data["id"],
    #                 "chapters": 0,
    #                 "number_season": 0,
    #             }

    #         data_season = SeasonRegisterSerializer(data=data_season)

    #         if data_season.is_valid():
    #             data_season.save()

    #         return Response(
    #             {"message": "Temporada registrada correctamente"},
    #             status=status.HTTP_201_CREATED,
    #         )
    #     return Response(
    #         {"message": "Hay errores en el registro", "error": serializer.errors},
    #         status=status.HTTP_400_BAD_REQUEST,
    #     )

    def retrieve(self, request, pk=None):
        season = self.get_object(pk)
        season_serializer = self.serializer_class(season)
        return Response(season_serializer.data)

    def update(self, request, pk=None):
        season = self.get_object(pk)
        season_serializer = self.serializer_class(season, data=request.data)
        if season_serializer.is_valid():
            season_serializer.save()
            return Response(
                {"message": "Temporada actualizada correctamente"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "message": "Hay errores en la actualización",
                "error": season_serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def destroy(self, request, pk=None):
        season_destroy = self.serializer_class.Meta.model.objects.filter(id=pk).update(
            state=False
        )
        if season_destroy == 1:
            return Response(
                {"message": "Temporada eliminada correctamente!"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"message": "No existe la temporada que desea eliminar"},
            status=status.HTTP_404_NOT_FOUND,
        )

    def partial_update(self, request, pk=None):
        """Update with data of the serie's season"""

        season = self.get_object(pk)
        season_serializer = SeasonUpdateSerializer(season, data=request.data, partial=True)
        if season_serializer.is_valid():
            season_serializer.save()
            return Response(
                {"message": "Temporada actualizada correctamente"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "message": "Hay errores en la actualización",
                "error": season_serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
