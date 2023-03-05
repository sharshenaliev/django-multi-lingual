from django.db import models
from ckeditor.fields import RichTextField
from parler.models import TranslatableModel, TranslatedFields


class Components(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=50),
        description=RichTextField(blank=True)
    )
    image = models.ImageField(upload_to='images/gallery', blank=True)

    class Meta:
        verbose_name = "Компонент"
        verbose_name_plural = "Компоненты"


class Images(models.Model):
    image = models.ImageField(upload_to='images/home')

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"


class Advantages(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50),
        description=models.CharField(max_length=200)
    )
    icon = models.FileField(upload_to='images/icons')

    class Meta:
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"


class Exams(TranslatableModel):
    translations = TranslatedFields(
        tag=models.CharField(max_length=30),
        name=RichTextField(),
        description=RichTextField()
    )
    image_one = models.ImageField(upload_to='images/gallery')
    image_two = models.ImageField(upload_to='images/gallery')

    class Meta:
        verbose_name = "Экзамен"
        verbose_name_plural = "Экзамены"


class Videos(models.Model):
    url = models.URLField()

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"


class Contacts(models.Model):
    address = models.URLField()
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    telegram = models.URLField()
    whatsapp = models.URLField()
    instagram = models.URLField()

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class Icons(models.Model):
    icon = models.FileField(upload_to='images/icons')

    class Meta:
        verbose_name = "Иконка"
        verbose_name_plural = "Иконки"
