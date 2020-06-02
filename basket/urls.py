from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_basket, name="view_basket"),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('remove/<item_id>/', views.remove, name='remove'),

]
