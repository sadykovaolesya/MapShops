from django.contrib import admin

from .models import City, Shop, ShopBuilding, Street

admin.site.register(ShopBuilding)
admin.site.register(Shop)
admin.site.register(Street)
admin.site.register(City)
