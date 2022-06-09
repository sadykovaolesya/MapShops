from typing import Any

from rest_framework import serializers

from .models import City, Shop, ShopBuilding, Street


class StreetSerializer(serializers.ModelSerializer):
    """Вывод списка улиц"""

    class Meta:
        model = Street
        fields = ("name",)


class CityListSerializer(serializers.ModelSerializer):
    """Вывод списка городов"""

    class Meta:
        model = City
        fields = ("name",)


class CityDetailSerializer(serializers.ModelSerializer):
    """Вывод списка улиц города"""

    street = StreetSerializer(many=True)

    class Meta:
        model = City
        fields = ("id", "name", "street")


class ShopSerializer(serializers.ModelSerializer):
    """Вывод названия магазина"""

    class Meta:
        model = Shop
        fields = ("name",)


class ShopListSerializer(serializers.ModelSerializer):
    """Вывод информации о магазине"""

    shop = ShopSerializer()
    city = CityListSerializer()
    street = StreetSerializer()
    open = serializers.BooleanField(source="get_shop_status", read_only=True)

    class Meta:
        model = ShopBuilding
        fields = "__all__"

    def create(self, validated_data) -> Any:
        """Добавление магазина"""
        name_shop_data = validated_data.pop("shop")
        city_data = validated_data.pop("city")
        street_data = validated_data.pop("street")

        name, created = Shop.objects.get_or_create(**name_shop_data)
        city, created = City.objects.get_or_create(**city_data)
        street, created = Street.objects.get_or_create(**street_data)
        street.city.add(city)

        shop_building = ShopBuilding.objects.create(
            shop=name, city=city, street=street, **validated_data
        )
        return shop_building
