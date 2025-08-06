from django.db import models
from products.models import Menu
from django.contrib.auth.models import User

class Order(models.Model):
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.menu_item.name} * {self.quantity}"

class Order(models.Model):
    STATUS_CHOICES = [

        ('PENDING','pending'),
        ('CONFIRMED','confirmed'),
        ('CANCELLED','cancelled'),
        ('DELIVERED','delevered'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_items = models.ManyToManyField(Menu)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=20, choices=STATUS_CHOICES,default='PENDING')
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.pk} by {self.customer.username}" 


