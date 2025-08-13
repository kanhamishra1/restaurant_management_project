from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('items/', ItemView.as_view(), name='item-list'),
    path('menu/' ,  , name='hardcoded_menu'),
    
]