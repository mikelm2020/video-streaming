from django.db import models

from apps.base.models import BaseModel
from apps.users.models import User
from apps.core.models import Provider
from apps.season.models import Season


class Playlist(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    video = models.ManyToManyField(Season, related_name="videos",through="PlaylistVideo")

    class Meta:
        verbose_name = "Lista de reproducción"
        verbose_name_plural = "Listas de reproducción"

    def str(self):
        return f"{self.pk} - {self.user.email} - {self.provider.provider}"


class PlaylistVideo(models.Model):
    playlist_id = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    season_id = models.ForeignKey(Season, on_delete=models.CASCADE)
    viewed = models.BooleanField(verbose_name="Visto", default=False)
    
    class Meta:
        db_table = "playlist_playlist_video_viewed"

    