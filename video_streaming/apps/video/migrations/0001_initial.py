# Generated by Django 4.1.2 on 2022-11-19 07:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("state", models.BooleanField(default=True, verbose_name="Estado")),
                (
                    "created_date",
                    models.DateField(
                        auto_now_add=True, verbose_name="Fecha de Creación"
                    ),
                ),
                (
                    "modified_date",
                    models.DateField(
                        auto_now=True, verbose_name="Fecha de Modificación"
                    ),
                ),
                (
                    "deleted_date",
                    models.DateField(
                        auto_now=True, verbose_name="Fecha de Eliminación"
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="Nombre")),
                ("num_year", models.IntegerField(verbose_name="Año")),
                (
                    "video_type",
                    models.CharField(
                        choices=[
                            ("S", "Serie"),
                            ("M", "Pelicula"),
                            ("D", "Documental"),
                            ("R", "Reality"),
                        ],
                        max_length=1,
                        verbose_name="Tipo",
                    ),
                ),
                ("duration", models.IntegerField(blank=True, verbose_name="Duración")),
                (
                    "classification",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.classification",
                        verbose_name="Clasificación",
                    ),
                ),
                (
                    "country",
                    models.ManyToManyField(to="core.country", verbose_name="Pais"),
                ),
                (
                    "film_genre",
                    models.ManyToManyField(
                        to="core.filmgenre", verbose_name="Genero Cinematográfico"
                    ),
                ),
                (
                    "provider",
                    models.ManyToManyField(
                        to="core.provider", verbose_name="Proveedor"
                    ),
                ),
            ],
            options={
                "verbose_name": "Video",
                "verbose_name_plural": "Videos",
            },
        ),
        migrations.CreateModel(
            name="HistoricalVideo",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                ("state", models.BooleanField(default=True, verbose_name="Estado")),
                (
                    "created_date",
                    models.DateField(
                        blank=True, editable=False, verbose_name="Fecha de Creación"
                    ),
                ),
                (
                    "modified_date",
                    models.DateField(
                        blank=True, editable=False, verbose_name="Fecha de Modificación"
                    ),
                ),
                (
                    "deleted_date",
                    models.DateField(
                        blank=True, editable=False, verbose_name="Fecha de Eliminación"
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="Nombre")),
                ("num_year", models.IntegerField(verbose_name="Año")),
                (
                    "video_type",
                    models.CharField(
                        choices=[
                            ("S", "Serie"),
                            ("M", "Pelicula"),
                            ("D", "Documental"),
                            ("R", "Reality"),
                        ],
                        max_length=1,
                        verbose_name="Tipo",
                    ),
                ),
                ("duration", models.IntegerField(blank=True, verbose_name="Duración")),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "classification",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="core.classification",
                        verbose_name="Clasificación",
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Video",
                "verbose_name_plural": "historical Videos",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
