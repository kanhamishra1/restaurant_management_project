from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name = 'home'),
    path('home1/', views.demo_home_page, name = 'new_home'),
    path('about/', views.about_view, name = 'about'),
    path('reservation/', views.reservation, name = 'reservation'),
    path('feedback/',views.feedback_view)
]