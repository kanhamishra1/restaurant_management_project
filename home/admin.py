from django.contrib import admin
from .models import RestaurantLocation
from .models import RestaurantInfo
from .models import MenuCategory


@admin.register(RestaurantLocation)
class RestaurantLocationAdmin(admin.ModelAdmin):
    list_display = ('address', 'city', 'state', 'zip_code')

admin.site.register(RestaurantInfo)

@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)