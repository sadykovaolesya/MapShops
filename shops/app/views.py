from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .models import City, ShopBuilding
from .serializers import CityDetailSerializer, CityListSerializer, ShopListSerializer
from .service import ShopFilter


class CityViewList(generics.ListAPIView):
    """Вывод списка городов"""

    queryset = City.objects.all()
    serializer_class = CityListSerializer


class CityViewDetail(generics.RetrieveAPIView):
    """Вывод списка улиц по городам"""

    queryset = City.objects.all()
    serializer_class = CityDetailSerializer


class ShopViews(generics.ListCreateAPIView):
    """Создание и вывод списка магазинов"""

    queryset = ShopBuilding.objects.all()
    serializer_class = ShopListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ShopFilter
