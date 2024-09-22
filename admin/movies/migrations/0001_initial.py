# Generated by Django 4.2.11 on 2024-06-19 16:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="description"),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Жанр",
                "verbose_name_plural": "Жанры",
                "db_table": 'content"."genre',
            },
        ),
    ]