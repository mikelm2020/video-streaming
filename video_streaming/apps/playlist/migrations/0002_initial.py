# Generated by Django 4.1.2 on 2022-11-19 07:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("core", "0002_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("playlist", "0001_initial"),
        ("season", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="playlist",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="playlist",
            name="video",
            field=models.ManyToManyField(to="season.season"),
        ),
        migrations.AddField(
            model_name="historicalplaylist",
            name="history_user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="historicalplaylist",
            name="provider",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="core.provider",
            ),
        ),
        migrations.AddField(
            model_name="historicalplaylist",
            name="user",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]