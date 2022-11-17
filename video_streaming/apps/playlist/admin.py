from django.contrib import admin
from apps.playlist.models import Playlist, VideoPlaylist




class VideoPlaylistInline(admin.TabularInline):
    model = VideoPlaylist
    extra = 1
    autocomplete_fields = ['video']


class PlaylistAdmin(admin.ModelAdmin):
    inlines = [
        VideoPlaylistInline,
    ]
    filter_horizontal = [
        "video",
    ]

admin.site.register(Playlist, PlaylistAdmin)
