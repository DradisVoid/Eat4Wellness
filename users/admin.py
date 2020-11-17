from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


# Register your models here.
class MyUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('is_member', 'is_coach', 'is_admin')
    list_filter = UserAdmin.list_filter + ('is_member', 'is_coach', 'is_admin')
    fieldsets = UserAdmin.fieldsets + (('User Type', {
        'fields': ('is_member', 'is_coach', 'is_admin')
    }),)


admin.site.register(User, MyUserAdmin)
admin.site.register(Coach)
admin.site.register(Member)
admin.site.register(Admin)
