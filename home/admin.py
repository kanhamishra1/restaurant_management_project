from django.contrib import admin
from .models import RestaurantLocation
from .models import RestaurantInfo

@admin.register(RestaurantLocation)
class RestaurantLocationAdmin(admin.ModelAdmin):
    list_display = ('address', 'city', 'state', 'zip_code')

admin.site.register(RestaurantInfo)

