from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_gifts, name="gifts"),
     path('<int:gift_id>', views.gift, name='gift'),

]