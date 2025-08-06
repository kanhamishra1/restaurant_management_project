from django.contrib import admin
from .models import Menu
from .models import Item


admin.site.register(Menu)
admin.site.register(Order)


# Custom Admins
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_name','item_price','created_at']


# Register your models here.
admin.site.register(Item,ItemAdmin)