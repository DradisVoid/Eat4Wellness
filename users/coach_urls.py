"""
App specific urls
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='coach_homepage'),
    path('member_data/', views.MemberListView.as_view(), name='coach_view_members'),
    path('member_data/<int:pk>', views.MemberDetailView.as_view(), name='member-detail-view'),
]
