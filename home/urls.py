from django.urls import path
from . import views

urlpatterns = [
    path('', home_view, name = 'home'),
    path('home1/', demo_home_page, name = 'new_home'),
    path('about/', about_view, name = 'about')
]