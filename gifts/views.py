from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Gift, Category
# Create your views here.
def all_gifts(request):
    gifts = Gift.objects.all()

    context = {
        'gifts': gifts,
    }

    return render(request,'gifts/gifts.html', context)

def gift(request, gift_id):

    gift = get_object_or_404(Gift, pk=gift_id)

    context = {
        'gift': gift
    }
    return render(request, 'gifts/single_gift.html', context)