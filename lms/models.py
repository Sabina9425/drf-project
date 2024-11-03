from django.db import models


class Course(models.Model):
    name = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        verbose_name="Имя курса",
        help_text="Введите имя курса",
    )
    description = models.TextField(
        max_length=100,
        verbose_name="Описание курса",
        help_text="Введите описание курса",
    )
    image = models.ImageField(
        upload_to="courses/photo",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите фото курса",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Имя урока", help_text="Введите имя урока"
    )
    description = models.TextField(
        max_length=100,
        verbose_name="Описание курса",
        help_text="Введите описание урока",
    )
    image = models.ImageField(
        upload_to="lessons/photo",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите фото урока",
    )
    video_link = models.CharField(
        verbose_name="Ссылка на видео", help_text="Введите ссылку на видео"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Курс",
        help_text="Введите курс",
        related_name="уроки",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.name
