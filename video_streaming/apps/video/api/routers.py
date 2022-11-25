from rest_framework.routers import DefaultRouter

from apps.video.api.video_viewsets import VideoNewViewSet

router = DefaultRouter()
router.register(r"videos", VideoNewViewSet, basename="videos")
urlpatterns = router.urls
