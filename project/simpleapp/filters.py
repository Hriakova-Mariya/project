from django_filters import FilterSet
from .models import Product


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],  # поиск по названию
            'quantity': ['gt'],  # количество товаров должно быть больше или равно
            'price': [
                'lt',  # цена должна быть меньше или равна указанной
                'gt',  # цена должна быть больше или равна указанной
            ]
        }
