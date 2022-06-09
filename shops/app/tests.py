from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import City, Shop, ShopBuilding, Street
from .serializers import CityDetailSerializer


class ShopsTests(APITestCase):
    def setUp(self) -> None:
        self.one_city = City.objects.create(name="Москва")
        self.one_street = Street.objects.create(name="Парковая")
        self.one_street.city.add(self.one_city)

        self.one_shop = Shop.objects.create(name="DNS")
        self.one_shop_buiding = ShopBuilding.objects.create(
            city=self.one_city,
            street=self.one_street,
            shop=self.one_shop,
            building=1,
            time_open="09:30",
            time_close="21:00",
        )

        self.data = {
            "shop": {"name": "Pink"},
            "city": {"name": "Омск"},
            "street": {"name": "Лесная"},
            "building": "10",
            "time_open": "09:00",
            "time_close": "21:00",
        }

    def test_cities_list(self):
        response = self.client.get(reverse("city_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        self.assertEqual(len(response.data), 1)

    def test_city_db(self):
        city = City.objects.get(id=self.one_city.id)
        self.assertEqual(city.name, "Москва")

    def test_city_detail(self):
        response = self.client.get(
            reverse("city_streets", kwargs={"pk": self.one_city.id})
        )
        serializer_data = CityDetailSerializer(self.one_city).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data)

    def test_create_shop(self):
        response = self.client.post(reverse("shop"), self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_shops_list(self):
        response = self.client.get(reverse("shop"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        self.assertEqual(len(response.data), 1)
