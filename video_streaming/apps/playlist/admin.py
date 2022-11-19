from django.contrib import admin
from apps.playlist.models import Playlist


class PlaylistAdmin(admin.ModelAdmin):

    filter_horizontal = [
        "video",
    ]


admin.site.register(Playlist, PlaylistAdmin)
