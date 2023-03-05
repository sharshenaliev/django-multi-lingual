from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class OurTeam(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50),
        position=models.CharField(max_length=40)
    )
    image = models.ImageField(upload_to='images/team')

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
