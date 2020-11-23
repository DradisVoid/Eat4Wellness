"""
App specific urls
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='member_homepage'),
    path('add_meal/', views.meal_add, name='member_add_meal'),
    path('compare_food/', views.food_compare, name='member_compare_meal'),
]
