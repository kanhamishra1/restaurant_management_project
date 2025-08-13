from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name = 'home'),
    path('home1/', demo_home_page,  )
    path('about/', about_view, name = 'about')
]