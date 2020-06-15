from django.shortcuts import render, HttpResponse
from .models import Gift, Category
# Create your views here.
def all_gifts(request):

    return render(request,'gifts/gifts.html')