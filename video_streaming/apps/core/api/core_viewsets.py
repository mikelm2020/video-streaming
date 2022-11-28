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
from rest_framework import filters, viewsets


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
