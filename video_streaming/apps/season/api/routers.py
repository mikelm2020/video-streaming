from apps.season.api.season_viewsets import SeasonViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"seasons", SeasonViewSet, basename="seasons")
urlpatterns = router.urls
