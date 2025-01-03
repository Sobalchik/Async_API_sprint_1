# Generated by Django 4.2.11 on 2024-06-30 20:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0006_filmwork_certificate_filmwork_file_path"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="filmwork",
            options={"verbose_name": "film", "verbose_name_plural": "films"},
        ),
        migrations.AlterModelOptions(
            name="genre",
            options={"verbose_name": "genre", "verbose_name_plural": "genres"},
        ),
        migrations.AlterModelOptions(
            name="person",
            options={"verbose_name": "actor", "verbose_name_plural": "actors"},
        ),
        migrations.AlterField(
            model_name="filmwork",
            name="certificate",
            field=models.CharField(
                blank=True, max_length=512, null=True, verbose_name="certificate"
            ),
        ),
        migrations.AlterField(
            model_name="filmwork",
            name="creation_date",
            field=models.DateField(verbose_name="creation date"),
        ),
        migrations.AlterField(
            model_name="filmwork",
            name="description",
            field=models.TextField(blank=True, verbose_name="description"),
        ),
        migrations.AlterField(
            model_name="filmwork",
            name="rating",
            field=models.FloatField(
                blank=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(100),
                ],
                verbose_name="rating",
            ),
        ),
        migrations.AlterField(
            model_name="filmwork",
            name="title",
            field=models.CharField(max_length=255, verbose_name="title"),
        ),
        migrations.AlterField(
            model_name="filmwork",
            name="type",
            field=models.CharField(
                choices=[("фильмы", "Movies"), ("телешоу", "Tv Shows")],
                default="фильмы",
                verbose_name="type",
            ),
        ),
        migrations.AlterField(
            model_name="genre",
            name="description",
            field=models.TextField(blank=True, verbose_name="description"),
        ),
        migrations.AlterField(
            model_name="genre",
            name="name",
            field=models.CharField(max_length=255, verbose_name="name"),
        ),
        migrations.AlterField(
            model_name="person",
            name="full_name",
            field=models.CharField(max_length=512, verbose_name="full name"),
        ),
        migrations.AlterField(
            model_name="personfilmwork",
            name="role",
            field=models.TextField(verbose_name="role"),
        ),
    ]
