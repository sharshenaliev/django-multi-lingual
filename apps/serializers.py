from .models.home import *
from .models.aboutus import *
from .models.studyabroad import *
from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from .mixins import TranslatedSerializerMixin


class ImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'


class VideosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = '__all__'


class IconsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Icons
        fields = '__all__'


class PhotosSerializers(serializers.ModelSerializer):
    class Meta:
        model = EducationPhotos
        fields = '__all__'


class ContactsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class ComponentsSerializers(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Components)

    class Meta:
        model = Components
        fields = '__all__'


class AdvantagesSerializers(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Advantages)

    class Meta:
        model = Advantages
        fields = '__all__'


class ExamsSerializers(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Exams)

    class Meta:
        model = Exams
        fields = '__all__'


class OurTeamSerializers(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=OurTeam)

    class Meta:
        model = OurTeam
        fields = '__all__'


class CountriesSerializers(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Countries)

    class Meta:
        model = Countries
        fields = '__all__'


class CategorySerializers(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Category)

    class Meta:
        model = Category
        fields = '__all__'


class SpecializationSerializers(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Specialization)

    class Meta:
        model = Specialization
        fields = '__all__'


class LanguagesSerializers(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Languages)

    class Meta:
        model = Languages
        fields = '__all__'


class EducationCentersSerializers(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=EducationCenters)

    class Meta:
        model = EducationCenters
        fields = '__all__'
