from ..serializers import *
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet


class Components(ListAPIView):
    serializer_class = ComponentsSerializers
    queryset = Components.objects.all()


class Images(ListAPIView):
    serializer_class = ImagesSerializers
    queryset = Images.objects.all()


class Videos(ListAPIView):
    serializer_class = VideosSerializers
    queryset = Videos.objects.all()


class Icons(ListAPIView):
    serializer_class = IconsSerializers
    queryset = Icons.objects.all()


class Advantages(ListAPIView):
    serializer_class = AdvantagesSerializers
    queryset = Advantages.objects.all()


class ExamsViewset(ReadOnlyModelViewSet):
    serializer_class = ExamsSerializers
    queryset = Exams.objects.all()


class Contacts(ListAPIView):
    serializer_class = ContactsSerializers
    queryset = Contacts.objects.all()
