from rest_framework.routers import DefaultRouter

from apps.video.api.video_viewsets import VideoViewSet

router = DefaultRouter()
router.register(r"", VideoViewSet, basename="videos")
urlpatterns = router.urls
