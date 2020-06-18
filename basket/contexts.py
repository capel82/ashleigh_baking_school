from django.conf import settings
from django.shortcuts import get_object_or_404
from courses.models import Course

def basket_contents(request):

    basket_items = []
    total = 0
    item_count = 0
    basket = request.session.get('basket', {})

    for item_id, item_data in basket.items():
        course = get_object_or_404(Course, pk=item_id)

        total += item_data * course.price
        subtotal = item_data * course.price
        item_count += item_data
        basket_items.append({
            'item_id': item_id,
            'quantity': item_data,
            'subtotal': subtotal,
            'course': course,
        })

    grand_total = total

    context = {
        'basket_items': basket_items,
        'item_count': item_count,
        'grand_total': grand_total,
    }

    return context