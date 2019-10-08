import django_filters

from . import models


class CompanyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = models.Company
        fields = ['name', 'phone', 'email', 'state', ]
