from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #User already have a email field
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_field=15, blank=True)

    def __str__(self):
        return self.user.username


        
    



