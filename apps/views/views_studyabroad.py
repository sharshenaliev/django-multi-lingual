from ..serializers import *
from ..service import SpecializationFilter
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class Countries(ListAPIView):
    serializer_class = CountriesSerializers
    queryset = Countries.objects.all()


class Category(ListAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()


class Specialization(ListAPIView):
    serializer_class = SpecializationSerializers
    queryset = Specialization.objects.all()


class Languages(ListAPIView):
    serializer_class = LanguagesSerializers
    queryset = Languages.objects.all()


class Photos(ListAPIView):
    serializer_class = PhotosSerializers
    queryset = EducationPhotos.objects.all()


class Centers(ListAPIView):
    serializer_class = EducationCentersSerializers
    queryset = EducationCenters.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = SpecializationFilter
    filterset_fields = ['country', 'category', 'specialization']
    search_fields = ['translations__name', ]
