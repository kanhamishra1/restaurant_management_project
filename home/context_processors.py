import datetime
from django.conf import settings

def current_year(request):
    return {'current_year': datetime.datetime.now().year}

def restaurant_name(request):
    return {"RESTAURANT_NAME" : getattr(settings, "RESTAURANT_NAME", "restaurant")}