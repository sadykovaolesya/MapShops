from datetime import datetime

from django.db import models


class BaseModel(models.Model):
    """Абстрактная модель"""

    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name


class City(BaseModel):
    """Модель города"""

    pass


class Shop(BaseModel):
    """Модель магазина"""

    pass


class Street(BaseModel):
    """Модель улицы"""

    city = models.ManyToManyField(City, related_name="street")


class ShopBuilding(models.Model):
    """Модель информации о магазине"""

    shop = models.ForeignKey(
        Shop, on_delete=models.CASCADE, related_name="shop_building"
    )
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="shop_building"
    )
    street = models.ForeignKey(
        Street, on_delete=models.CASCADE, related_name="shop_building"
    )
    building = models.CharField(max_length=5)
    time_open = models.TimeField()
    time_close = models.TimeField()

    def __str__(self) -> str:
        return f"{self.firstName} {self.secondName}"

    def get_shop_status(self) -> bool:
        """Метод получения статуса магазина (открыт/закрыт)"""
        open = self.time_open.strftime("%H:%M")
        close = self.time_close.strftime("%H:%M")
        time_now = datetime.now().strftime("%H:%M")
        return open < time_now < close

    class Meta:
        unique_together = ["shop", "city", "street", "building"]
