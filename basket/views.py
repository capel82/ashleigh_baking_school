from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def view_basket(request):
    return render(request, 'basket/basket.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity
    request.session['basket'] = basket
    return redirect(redirect_url)

def remove(request, item_id):

    basket = request.session.get('basket', {})

    basket.pop(item_id)

    request.session['basket'] = basket

    return render(request, 'basket/basket.html')
