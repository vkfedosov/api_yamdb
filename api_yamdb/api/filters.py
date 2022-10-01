from django_filters.rest_framework import CharFilter, FilterSet

from titles.models import Title


class TitleFilter(FilterSet):
    """Фильтр по полям произведений."""
    name = CharFilter(field_name='name', lookup_expr='icontains')
    category = CharFilter(
        field_name='category__slug', lookup_expr='icontains'
    )
    genre = CharFilter(
        field_name="genre__slug", lookup_expr='icontains'
    )

    class Meta:
        model = Title
        fields = ('name', 'year', 'category', 'genre')
