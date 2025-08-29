from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('items/', ItemView.as_view(), name='item-list'),
    path('menu/' , views.menu_view, name='menu_items'),
    
]