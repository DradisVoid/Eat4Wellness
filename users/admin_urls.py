"""
App specific urls
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='admin_homepage'),
    path('analytics/', views.admin_analytics, name='admin_analytics'),
    path('add_user/', views.admin_add_user, name='admin_add_user'),
]
