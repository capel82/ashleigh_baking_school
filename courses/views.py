from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import Course, Category

def all_courses(request):
    """ A view to show all courses, filter by category and pagination """

    courses = Course.objects.order_by('weekends_datetime').filter(is_published=True)
    query = None
    category = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            courses = courses.filter(category__title__in=categories)
            categories = Category.objects.filter(title__in=categories)

    paginator = Paginator (courses, 6)
    page = request.GET.get('page')

    paged_courses = paginator.get_page(page)

    context = {
        'courses': paged_courses,
        'current_categories': category,
    }
    return render(request, 'courses/courses.html', context)

def course(request, course_id):

    course = get_object_or_404(Course, pk=course_id)

    content = {
        'course': course
    }
    return render(request, 'courses/individual_course.html', content)