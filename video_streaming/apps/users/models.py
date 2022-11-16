from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from simple_history.models import HistoricalRecords

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(
        "Correo Electrónico",
        max_length=255,
        unique=True,
    )
    name = models.CharField("Nombre", max_length=255, blank=True, null=True)
    last_name = models.CharField("Apellidos", max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    historical = HistoricalRecords()
    objects = UserManager()

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "name", "last_name"]

    def __str__(self):
        return f"{self.name} {self.last_name}"
