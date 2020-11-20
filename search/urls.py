"""
App specific urls
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_food, name='search_food')
]
