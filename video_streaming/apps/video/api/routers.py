from apps.video.api.video_viewsets import VideoNewViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"videos", VideoNewViewSet, basename="videos")
urlpatterns = router.urls
