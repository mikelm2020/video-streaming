from apps.playlist.api.playlist_viewsets import PlaylistVideoViewSet, PlaylistViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"playlists", PlaylistViewSet, basename="playlist")
router.register(
    r"videos-in-playlists", PlaylistVideoViewSet, basename="videos_in_playlist"
)
urlpatterns = router.urls
