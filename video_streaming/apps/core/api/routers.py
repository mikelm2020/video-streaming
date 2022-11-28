from apps.core.api.core_viewsets import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"filmgenres", FilmGenreViewSet, basename="film_genres")
router.register(r"classifications", ClassificationViewSet, basename="classifications")
router.register(r"countries", CountryViewSet, basename="countries")
router.register(r"providers", ProviderViewSet, basename="providers")

urlpatterns = router.urls
