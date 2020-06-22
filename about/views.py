from django.shortcuts import render
from .models import Team

def team(request):

    teams = Team.objects.all()

    context = {
        'teams': teams,
    }

    return render(request, 'about/team.html', context)

def kitchen(request):

    return render(request, 'about/kitchen.html')

def faqs(request):

    return render(request, 'about/faqs.html')