from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponseServerError
from django.core.mail import send_mail
from .forms import ContactForm, FeedbackForm  
from .models import RestaurantLocation
from products.models import MenuItem


# This is home page section
def home(request):
    restaurant = RestaurantLocation.objects.first()

   
    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())

    context = {
        "restaurant": restaurant,
        "cart_count": cart_count,
    }
    return render(request, 'home/home.html', context)


# This is for About page
def about_view(request):
    return render(request, 'home/about.html')


# This is for reservation section
def reservation(request):
    try:
        return render(request, 'home/reservation.html')
    except Exception as e:
        print(f"Error in reservation view: {e}")
        return HttpResponseServerError("<h1>Something went wrong!</h1><p>Please try again later</p>")

# This is feedback section
def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FeedbackForm()

    return render(request, 'home/contact.html', {'form': form})

# This is for menu item search
def search(request):
    restaurant = RestaurantLocation.objects.first()
    query = request.GET.get("q", "")
    if query:
        menu_items = MenuItem.objects.filter(name__icontains=query)
    else:
        menu_items = MenuItem.objects.all()

    context = {
        "restaurant": restaurant,
        "menu_items": menu_items,
        "query": query,
    }
    return render(request, "home/home.html", context)

# This is for contact section
def email_contact_view(request):
    restaurant = RestaurantLocation.objects.first()
    menu_items = MenuItem.objects.all()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                subject=f"New Contact Form Submission from {name}",
                message=f"Name: {name}\nEmail: {email}\nMessage:\n{message}",
                from_email=email,
                recipient_list=["TestyBites@gmail.com"],
            )
            return redirect("home")
    else:
        form = ContactForm()

    return render(request, "home/home.html", {
        "restaurant": restaurant,
        "menu_items": menu_items,
        "form": form,
    })
