from django.urls import path

from . import views

urlpatterns = [
    path('team', views.team, name="team"),
    path('kitchen', views.kitchen, name="kitchen"),
    path('faqs', views.faqs, name="faqs"),
]