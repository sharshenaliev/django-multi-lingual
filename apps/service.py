from .models.studyabroad import Specialization
import django_filters


class SpecializationFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        name='specialization__name',
        lookup_type='contains',
    )

    class Meta:
        model = Specialization
        fields = ['name', ]
