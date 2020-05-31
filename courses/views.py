from django.shortcuts import render, get_object_or_404
from .models import Course

def all_courses(request):
    """ A view to show all courses, including sorting and search queries """

    courses = Course.objects.all()

    context = {
        'courses': courses,
    }

    return render(request, 'courses/courses.html', context)

def course(request, course_id):

    course = get_object_or_404(Course, pk=course_id)

    content = {
        'course' : course
    }
    return render(request, 'courses/individual_course.html', content)