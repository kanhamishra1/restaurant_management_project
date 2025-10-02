from django.urls import path
from .views import RiderRegisterView, DriverRegisterView

urlpatterns = [
    path('api/register/rider/', RiderRegisterView.as_view(), name='rider-register'),
    path('api/register/driver/', DriverRegisterView.as_view(), name='driver-register'),
]
