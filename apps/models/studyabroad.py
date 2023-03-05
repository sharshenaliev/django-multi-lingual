from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from ckeditor.fields import RichTextField


class Countries(TranslatableModel):
    translations = TranslatedFields(
        country=models.CharField(max_length=40)
    )
    flag = models.ImageField(upload_to='images/flags')

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"

    def __str__(self):
        return self.country


class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Specialization(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"

    def __str__(self):
        return self.name


class Languages(TranslatableModel):
    translations = TranslatedFields(
        language=models.CharField(max_length=40)
    )

    class Meta:
        verbose_name = "Язык"
        verbose_name_plural = "Языки"

    def __str__(self):
        return self.language


class EducationCenters(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50),
        location=models.CharField(max_length=50),
        cost=RichTextField(),
        label=models.CharField(max_length=50),
        title=models.CharField(max_length=70),
        duratuon=models.CharField(max_length=70),
        awards=models.TextField(),
        tuition_fee=models.CharField(max_length=70),
        application_fee=models.CharField(max_length=70),
        registration_fee=models.TextField(),
        tuition=models.TextField(),
        entry_qualification=models.TextField(),
        semester=models.CharField(max_length=50),
        pre_deadline=models.CharField(max_length=100),
        deadline=models.CharField(max_length=100),
        age=models.CharField(max_length=50)
    )
    image_1 = models.ImageField(upload_to='images/education')
    image_2 = models.ImageField(upload_to='images/education')
    image_3 = models.ImageField(upload_to='images/education')
    foundation = models.IntegerField()
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)
    specialization = models.ManyToManyField(Specialization)
    language = models.ManyToManyField(Languages)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    commence = models.DateField()

    class Meta:
        verbose_name = "Учебное заведение"
        verbose_name_plural = "Учебные заведения"

    def __str__(self):
        return self.name


class EducationPhotos(models.Model):
    education_center = models.ForeignKey(EducationCenters, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/education/gallery')

    class Meta:
        verbose_name = "Фото заведения"
        verbose_name_plural = "Фото заведения"
