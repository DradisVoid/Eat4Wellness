from django.contrib import admin
from .models import ApiGetCall, ApiSearchCall

# Register your models here.
admin.site.register(ApiGetCall)
admin.site.register(ApiSearchCall)