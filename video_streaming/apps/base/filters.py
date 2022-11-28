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
