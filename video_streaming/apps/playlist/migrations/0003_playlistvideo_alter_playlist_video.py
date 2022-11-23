# Generated by Django 4.1.2 on 2022-11-22 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("season", "0002_initial"),
        ("playlist", "0002_initial"),
    ]

    state_operations = [
        migrations.CreateModel(
            name="PlaylistVideo",
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
                (
                    "playlist_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="playlist.playlist",
                    ),
                ),
                (
                    "season_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="season.season"
                    ),
                ),
                (
                    "viewed",
                    models.BooleanField(default=False, verbose_name="Visto"),
                ),
            ],
            options={
                "db_table": "playlist_playlist_video_viewed",
            },
        ),
        migrations.AlterField(
            model_name="playlist",
            name="video",
            field=models.ManyToManyField(
                related_name="videos",
                through="playlist.PlaylistVideo",
                to="season.season",
            ),
        ),
    ]
    operations = [
        migrations.SeparateDatabaseAndState(state_operations=state_operations),
    ]