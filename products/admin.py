from django.contrib import admin
from .models import *
from .models import Menu

admin.site.register(Menu)


# Custom Admins
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_name','item_price','created_at']


# Register your models here.
admin.site.register(Item,ItemAdmin)