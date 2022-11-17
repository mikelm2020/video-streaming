from apps.playlist.api.playlist_viewsets import PlaylistViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"playlists", PlaylistViewSet, basename="playlist")
urlpatterns = router.urls
