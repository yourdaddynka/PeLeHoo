from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['id', 'username', 'email', 'is_staff']
    search_fields = ['email', 'username']
    ordering = ['id']

admin.site.register(CustomUser, CustomUserAdmin)
