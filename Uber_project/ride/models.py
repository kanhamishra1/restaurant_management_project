from django.db import models


from django.contrib.auth.models import User  # using default Django User model

class Rider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="rider_profile")
    phone_number = models.CharField(max_length=15)
    preferred_payment_method = models.CharField(max_length=50, choices=[
        ("cash", "Cash"),
        ("card", "Card"),
        ("upi", "UPI"),
        ("wallet", "Wallet")
    ], default="cash")
    default_pickup_location = models.CharField(max_length=255, blank=True, null=True)
    profile_photo = models.ImageField(upload_to="riders/profile_photos/", blank=True, null=True)

    def __str__(self):
        return f"Rider: {self.user.username}"


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="driver_profile")
    phone_number = models.CharField(max_length=15)
    vehicle_make = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length=50)
    number_plate = models.CharField(max_length=20, unique=True)
    license_number = models.CharField(max_length=50, unique=True)
    availability_status = models.BooleanField(default=True)  # True = Available, False = Busy/Offline
    current_latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    current_longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    profile_photo = models.ImageField(upload_to="drivers/profile_photos/", blank=True, null=True)

    def __str__(self):
        return f"Driver: {self.user.username} ({self.number_plate})"
