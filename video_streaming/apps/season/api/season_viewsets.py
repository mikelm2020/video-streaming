from apps.base.pagination import ExtendedPagination
from apps.core.models import *
from apps.season.api.season_serializers import (
    SeasonCreateSerializer,
    SeasonSerializer,
    SeasonUpdateSerializer,
)
from apps.season.models import Season
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response


class SeasonViewSet(viewsets.GenericViewSet):
    serializer_class = SeasonSerializer
    pagination_class = ExtendedPagination

    def get_queryset(self, pk=None):
        if pk is None:
            return Season.objects.filter(state=True, video__video_type="S")
        else:
            return Season.objects.filter(id=pk, state=True).first()

    def get_object(self, pk):
        return get_object_or_404(Season, pk=pk)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = SeasonCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Temporada registrada correctamente"},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"message": "Hay errores en el registro", "error": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def retrieve(self, request, pk=None):
        season = self.get_object(pk)
        season_serializer = self.serializer_class(season)
        return Response(season_serializer.data)

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
        season_serializer = SeasonUpdateSerializer(
            season, data=request.data, partial=True
        )
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
