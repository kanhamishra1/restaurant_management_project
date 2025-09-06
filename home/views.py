from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponseServerError
from .forms import ContactForm,EmailContact
from .models import RestaurantLocation
from products.models import MenuItem



def home(request):
    restaurant = RestaurantLocation.objects.first()


    restaurant ={
        "name" = "Testy Bites",
        "opening_hours" = {
            "Mon-Fri": "11am - 9pm",
            "Sat-sun": "10am - 10pm"
        }
    }
    return render(request, 'home.html', {'restaurant': restaurant})


def home_view(request):
    context = {
        'restaurant_name': settings.RESTAURANT_NAME
    }
    return render(request, 'home/home.html', context)

def demo_home_page(request):
    restaurant_name = "Testy Bites"
    return render(request, 'home/home1.html', {'restaurant_name' : restaurant_name})

# For about section

def about_view(request):
    return render(request, 'home/about.html')

# For Reservation

def reservation(request):
    try:
        return render(request, 'home/reservation.html')
    except Exception as e:
        # Log the error for debugging
        print(f"Error in reservation view: {e}")
        return HttpResponseServerError(
            "<h1>Something went wrong!</h1><p>Please try again later</p>"
        )


# for feedback

def FeedbackForm(request):
    if request.method == "POST":
        form = Feedbackform(request.POST)
        if form.is_valid():
            form.save() #Save feedback into DB
            return redirect('home')

    else:
        form = ContactForm()

    return render(request, 'home/contact.html', {'form': form})


# for search items

def search(request):
    restaurant = Restaurant.objects.first()
    query = request.GET.get("q")

    if query:
        menu_items = MenuItem.objects.filter(name_icontains=query) # case insensitive search
    else:
        menu_items = MenuItem.objects.all()

    context = {
        "restaurant": restaurant,
        "menu_items": menu_items,
        "query": query,
    }
    return render(request, "home.html", context)

# For Email contact
 def EmailContact(request):
    if request.method == "POST":
        form = EmailContact(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email
            send_mail(
                subject=f"New Contact Form Submission from {name}",
                message=f"Name: {name}\nEmail: {email}\nMessage:\n{message}",
                from_email=email
                recipient_list=["TestyBites@gmail.com"],
            )

            return redirect("home")
    else:
        form = EmailContact()

    return render(request, "home.html",{
        "restaurant": restaurant,
        "menu_items": menu_items,
        "query": query,
        "form": form,
    })
