"""
App specific urls
"""

from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_food, name='search_food'),
    path('view/', views.get_nutrients, name='view_food')
]
