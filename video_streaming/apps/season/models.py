from django.db import models

from apps.base.models import BaseModel
from apps.video.models import Video

class Season(BaseModel):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    chapters = models.SmallIntegerField(verbose_name="Capitulos", default=0)
    number_season = models.SmallIntegerField(verbose_name="Temporada", default=0)
    

    class Meta:
        verbose_name = "Temporada"
        verbose_name_plural = "Temporadas"

    def str(self):
        return f"{self.video.name} S-{self.number_season}"
    