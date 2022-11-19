from django.db import models

from apps.base.models import BaseModel
from apps.users.models import User
from apps.core.models import Provider
from apps.season.models import Season


class Playlist(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    video = models.ManyToManyField(Season)

    class Meta:
        verbose_name = "Lista de reproducción"
        verbose_name_plural = "Listas de reproducción"

    def str(self):
        return f"{self.pk} - {self.user__email} - {self.provider__provider}"



