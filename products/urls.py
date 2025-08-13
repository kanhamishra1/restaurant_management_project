from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('items/', ItemView.as_view(), name='item-list'),
    path('menu/' , menu_item , name='hardcoded_menu'),
    
]