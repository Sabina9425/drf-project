# Generated by Django 5.1.2 on 2024-11-03 13:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
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
                    "name",
                    models.CharField(
                        blank=True,
                        help_text="Введите имя курса",
                        max_length=50,
                        null=True,
                        verbose_name="Имя курса",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Введите описание курса",
                        max_length=100,
                        verbose_name="Описание курса",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите фото курса",
                        null=True,
                        upload_to="courses/photo",
                        verbose_name="Превью",
                    ),
                ),
            ],
            options={
                "verbose_name": "Курс",
                "verbose_name_plural": "Курсы",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
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
                    "name",
                    models.CharField(
                        help_text="Введите имя урока",
                        max_length=50,
                        verbose_name="Имя урока",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Введите описание урока",
                        max_length=100,
                        verbose_name="Описание курса",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите фото урока",
                        null=True,
                        upload_to="lessons/photo",
                        verbose_name="Превью",
                    ),
                ),
                (
                    "video_link",
                    models.CharField(
                        help_text="Введите ссылку на видео",
                        verbose_name="Ссылка на видео",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        blank=True,
                        help_text="Введите курс",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="уроки",
                        to="lms.course",
                        verbose_name="Курс",
                    ),
                ),
            ],
            options={
                "verbose_name": "Урок",
                "verbose_name_plural": "Уроки",
            },
        ),
    ]
