import django_filters
from .models import Persona


class SnippetFilter(django_filters.FilterSet):
    dni = django_filters.CharFilter(label='Dni')
    codigocurso = django_filters.CharFilter(label='Curso')

    class Meta:
        model = Persona
        fields = ('dni', 'codigocurso')

