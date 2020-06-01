from django.conf import settings
from django.shortcuts import get_object_or_404
from courses.models import Course

def basket_contents(request):

    basket_items = []
    total = 0
    item_count = 0
    basket = request.session.get('basket', {})
    
    for course_id, quantity in basket.items():
        course = get_object_or_404(Course, pk=course_id)
        total += quantity * course.price
        item_count += quantity
        basket_items.append({
            'course_id': course_id,
            'quantity': quantity,
            'course': course,
        })

    grand_total = total
    
    context = {
        'basket_items': basket_items,
        'total': total,
        'item_count': item_count,
        'grand_total': grand_total,
    }

    return context