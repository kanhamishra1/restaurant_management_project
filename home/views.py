from django.conf import settings
from django.shortcuts import render


def home_view(request):
    context = {
        'restaurant_name': settings.RESTAURANT_NAME
    }
    return render(request, 'home/home.html', context)

def demo_home_page(request):
    context = {
        'restaurant_name': ""
    }

def about_view(request):
    return render(request, 'home/about.html')