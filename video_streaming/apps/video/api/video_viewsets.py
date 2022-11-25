from apps.core.models import *
from apps.video.api.filters import VideoFilterSet
from apps.video.api.pagination import ExtendedPagination
from apps.video.api.video_serializers import (
    SeasonRegisterSerializer,
    VideoSerializer,
    VideoStateSerializer,
)
from apps.video.models import Video
from django.db.models.query import QuerySet
from django_filters import rest_framework
from rest_framework import filters, status, viewsets
from rest_framework.response import Response


class VideoNewViewSet(viewsets.ModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.filter(state=True)
    filter_backends = [
        rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = VideoFilterSet
    search_fields = ("film_genre__film_genre", "name")
    ordering_fields = ("num_year",)
    pagination_class = ExtendedPagination

    def get_queryset(self):
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method." % self.__class__.__name__
        )

        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.all()
        return queryset

    def retrieve(self, request, *args, **kwargs):
        video = self.get_object(*args)
        video_serializer = self.serializer_class(video)
        return Response(video_serializer.data)

    def create(self, request, *args, **kwargs):
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

    def update(self, request, *args, **kwargs):
        video = self.get_object(*args)
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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, *args, **kwargs):
        """Unsubscribe a video"""
        video = self.get_object()
        video_serializer = VideoStateSerializer(video, data=request.data, partial=True)
        if video_serializer.is_valid():
            video_serializer.save()
            return Response(
                {"message": "Video dado de baja correctamente!"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "message": "Hay errores en la actualización",
                "error": video_serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
