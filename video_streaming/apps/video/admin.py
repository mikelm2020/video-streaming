from django.contrib import admin
from apps.video.models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):

    list_display = ("id", "name", "video_type")
    list_filter = ("video_type",)
    search_fields = ("name", "video_type")
    ordering = ("id", "name", "video_type")
