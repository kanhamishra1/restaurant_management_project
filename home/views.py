from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponseServerError
from .forms import ContactForm
from .models import 


def home_view(request):
    context = {
        'restaurant_name': settings.RESTAURANT_NAME
    }
    return render(request, 'home/home.html', context)

def demo_home_page(request):
    restaurant_name = "Testy Bites"
    return render(request, 'home/home1.html', {'restaurant_name' : restaurant_name})

def about_view(request):
    return render(request, 'home/about.html')

def reservation(request):
    try:
        return render(request, 'home/reservation.html')
    except Exception as e:
        # Log the error for debugging
        print(f"Error in reservation view: {e}")
        return HttpResponseServerError(
            "<h1>Something went wrong!</h1><p>Please try again later</p>"
        )

def ContactForm(request):
    if request.method == "POST":
        form = Feedbackform(request.POST)
        if form.is_valid():
            form.save() #Save feedback into DB
            return redirect('home')

    else:
        form = ContactForm()

    return render(request, 'home/contact.html', {'form': form})