from apps.base.filters import (
    ClassificationFilterSet,
    CountryFilterSet,
    FilmGenreFilterSet,
    ProviderFilterSet,
)
from apps.base.pagination import ExtendedPagination
from apps.core.api.core_serializers import *
from apps.core.models import *
from django.db.models.query import QuerySet
from django_filters import rest_framework
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import filters, viewsets
from rest_framework.response import Response


class FilmGenreViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FilmGenreSerializer
    queryset = FilmGenre.objects.filter(state=True)
    filter_backends = [
        rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = FilmGenreFilterSet
    search_fields = ("film_genre",)
    ordering_fields = ("film_genre",)
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

    @extend_schema(
        request=FilmGenreSerializer,
        parameters=[
            OpenApiParameter(
                name="ordering",
                location=OpenApiParameter.QUERY,
                description="The field can you use for ordering the results is: film_genre",
            ),
            OpenApiParameter(
                name="search",
                location=OpenApiParameter.QUERY,
                description="The field can you use for search is: film_genre",
            ),
        ],
    )
    def list(self, request, *args, **kwargs):
        """
        Get a collection of film genres
        """
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
        Get a film_genre
        """
        video = self.get_object(*args)
        video_serializer = self.serializer_class(video)
        return Response(video_serializer.data)


class ClassificationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ClassificationSerializer
    queryset = Classification.objects.filter(state=True)
    filter_backends = [
        rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = ClassificationFilterSet
    search_fields = ("age_rating",)
    ordering_fields = ("age_rating",)
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

    @extend_schema(
        request=ClassificationSerializer,
        parameters=[
            OpenApiParameter(
                name="ordering",
                location=OpenApiParameter.QUERY,
                description="The field can you use for ordering the results is: age_rating",
            ),
            OpenApiParameter(
                name="search",
                location=OpenApiParameter.QUERY,
                description="The field can you use for search is: age_rating",
            ),
        ],
    )
    def list(self, request, *args, **kwargs):
        """
        Get a collection of film's classifications
        """
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
        Get a classification
        """
        video = self.get_object(*args)
        video_serializer = self.serializer_class(video)
        return Response(video_serializer.data)


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.filter(state=True)
    filter_backends = [
        rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = CountryFilterSet
    search_fields = (
        "country",
        "iso_code",
    )
    ordering_fields = (
        "country",
        "iso_code",
    )
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

    @extend_schema(
        request=CountrySerializer,
        parameters=[
            OpenApiParameter(
                name="ordering",
                location=OpenApiParameter.QUERY,
                description="The fields can you use for ordering the results are: country and iso_code",
            ),
            OpenApiParameter(
                name="search",
                location=OpenApiParameter.QUERY,
                description="The fields can you use for search is: country and iso_code",
            ),
        ],
    )
    def list(self, request, *args, **kwargs):
        """
        Get a collection of countries
        """
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
        Get a country
        """
        video = self.get_object(*args)
        video_serializer = self.serializer_class(video)
        return Response(video_serializer.data)


class ProviderViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.filter(state=True)
    filter_backends = [
        rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = ProviderFilterSet
    search_fields = ("provider",)
    ordering_fields = ("provider",)
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

    @extend_schema(
        request=ProviderSerializer,
        parameters=[
            OpenApiParameter(
                name="ordering",
                location=OpenApiParameter.QUERY,
                description="The field can you use for ordering the results is: provider",
            ),
            OpenApiParameter(
                name="search",
                location=OpenApiParameter.QUERY,
                description="The field can you use for search is: provider",
            ),
        ],
    )
    def list(self, request, *args, **kwargs):
        """
        Get a collection of streaming providers
        """
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
        Get a streaming provider
        """
        video = self.get_object(*args)
        video_serializer = self.serializer_class(video)
        return Response(video_serializer.data)
