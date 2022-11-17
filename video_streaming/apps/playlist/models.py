from django.db import models

from apps.base.models import BaseModel
from apps.users.models import User
from apps.core.models import Provider
from apps.video.models import Video


class Playlist(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    video = models.ManyToManyField(Video, through="VideoPlaylist")
    viewed = models.BooleanField(verbose_name="Visto", default=False)

    class Meta:
        verbose_name = "Lista de reproducción"
        verbose_name_plural = "Listas de reproducción"

    def str(self):
        return f"{self.id} - {self.user.email} - {self.provider.provider}"


class VideoPlaylist(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    viewed = models.BooleanField(verbose_name="Visto", default=False)
