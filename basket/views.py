from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from courses. models import Course


# Create your views here.
def view_basket(request):
    return render(request, 'basket/basket.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    course = Course.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request, f'Updated {course.category}: {course.title} quantity')

    else:
        basket[item_id] = quantity
        messages.success(request, f' {course.category}: {course.title} added')

        request.session['basket'] = basket
    return redirect(redirect_url)

def update_basket(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
    else:
            basket.pop(item_id)

    request.session['basket'] = basket

    return redirect(reverse('view_basket'))

def remove(request, item_id):
    course = Course.objects.get(pk=item_id)
    basket = request.session.get('basket', {})
    basket.pop(item_id)

    request.session['basket'] = basket
    messages.warning(request, f'{course.category}: {course.title} removed')
    return render(request, 'basket/basket.html')