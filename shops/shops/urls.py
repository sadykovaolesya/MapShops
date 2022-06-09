from django.contrib import admin
from django.urls import path

from app.views import CityViewDetail, CityViewList, ShopViews

urlpatterns = [
    path("admin/", admin.site.urls),
    path("city/", CityViewList.as_view(), name="city_list"),
    path("city/<int:pk>/street/", CityViewDetail.as_view(), name="city_streets"),
    path("shop/", ShopViews.as_view(), name="shop"),
]
