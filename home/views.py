from django.shortcuts import render
from courses.models import Course

def index(request):
    #published course that is the next event and is published.
    courses = Course.objects.all().filter(is_published=True, 
            is_next_event=True)

    context = {
        'courses': courses
    }
    return render(request, 'home/index.html', context)
    