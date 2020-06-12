from django.shortcuts import render

# Create your views here.
def team(request):
    return render(request, 'about/team.html')

def kitchen(request):
    return render(request, 'about/kitchen.html')