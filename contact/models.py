from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=30, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    message = models.TextField(max_length=200, null=False, blank=False)
    contact_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    