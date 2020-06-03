import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings

from courses.models import Course

# Create your models here.
class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length = 200, null=False, blank=False)
    phone_number = models.CharField(max_length = 20, null=False, blank=False)
    street_address1 = models.CharField(max_length = 50, null=False, blank=False)
    street_address2 = models.CharField(max_length = 50, null=False, blank=True)
    town_or_city = models.CharField(max_length = 50, null=False, blank=False)
    county = models.CharField(max_length = 50, null=False, blank=False)
    country = models.CharField(max_length = 50, null=False, blank=False)
    postcode = models.CharField(max_length = 20, null=False, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    grand_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    course = models.ForeignKey(Course, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.course.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.course} on order {self.order.order_number}'