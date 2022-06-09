from datetime import datetime
from typing import Any

from django_filters import rest_framework as filters

from .models import ShopBuilding


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ShopFilter(filters.FilterSet):
    """Фильтр магазинов по городам, улицам, открыт/закрыт"""

    shop = CharFilterInFilter(field_name="shop__name", lookup_expr="in")
    city = CharFilterInFilter(field_name="city__name", lookup_expr="in")
    street = CharFilterInFilter(field_name="street__name", lookup_expr="in")
    open = filters.BooleanFilter(field_name="open", method="get_shop_open")

    def get_shop_open(self, queryset, field_name, value) -> Any:
        """Фильтр выводит открытые/закрытые магазины"""
        time_now = datetime.now().strftime("%H:%M")
        if value:
            return queryset.filter(time_open__lt=time_now, time_close__gt=time_now)
        else:
            return queryset.exclude(time_open__lt=time_now, time_close__gt=time_now)

    class Meta:
        model = ShopBuilding
        fields = ["shop", "city", "street", "open"]
