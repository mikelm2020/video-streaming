from apps.core.models import *
from apps.users.models import User
from apps.video.models import Video
from django_filters import rest_framework


class VideoFilterSet(rest_framework.FilterSet):
    name_is_like = rest_framework.CharFilter(field_name="name", lookup_expr="contains")
    genre_is_like = rest_framework.CharFilter(
        field_name="film_genre__film_genre", lookup_expr="contains"
    )
    classification_is_like = rest_framework.CharFilter(
        field_name="classification__age_rating", lookup_expr="contains"
    )
    provider_is = rest_framework.CharFilter(
        field_name="provider__provider", lookup_expr="contains"
    )
    country_is = rest_framework.CharFilter(
        field_name="country__iso_code", lookup_expr="contains"
    )

    class Meta:
        model = Video
        fields = (
            "video_type",
            "num_year",
        )


class UserFilterSet(rest_framework.FilterSet):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "name",
            "last_name",
        )


class FilmGenreFilterSet(rest_framework.FilterSet):
    film_genre_is = rest_framework.CharFilter(
        field_name="film_genre", lookup_expr="contains"
    )

    class Meta:
        model = FilmGenre
        fields = ("film_genre_is",)


class ClassificationFilterSet(rest_framework.FilterSet):
    classification_is = rest_framework.CharFilter(
        field_name="age_rating", lookup_expr="contains"
    )

    class Meta:
        model = Classification
        fields = ("classification_is",)


class CountryFilterSet(rest_framework.FilterSet):
    country_is = rest_framework.CharFilter(field_name="iso_code", lookup_expr="exact")

    class Meta:
        model = Country
        fields = ("country_is",)


class ProviderFilterSet(rest_framework.FilterSet):
    provider_is = rest_framework.CharFilter(
        field_name="provider", lookup_expr="contains"
    )

    class Meta:
        model = Provider
        fields = ("provider_is",)
