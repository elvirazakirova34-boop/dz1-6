from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('full_name', 'email', 'is_staff')
    
    list_filter = ('is_staff', 'is_active', 'role')
    ordering = ('email',)
    search_fields = ('full_name', 'email')

    fieldsets = (
        (None, {'fields': ('full_name', 'email', 'password')}),
        ('Личные данные', {'fields': ('is_staff', 'is_active', 'role', 'phone')}),
        ('Права доступа', {'fields': ('is_superuser', 'password1', 'password2')}),
    )