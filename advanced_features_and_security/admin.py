from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import CustomUser

class CustomUserAdmin(BaseUserAdmin):
    """
    A custom Admin class for the CustomUser model.
    It adds the date_of_birth and profile_photo fields to the user
    admin page.
    """
    # The list_display will show these fields in the user list view
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'date_of_birth')

    # The fieldsets will organize the fields in the user detail form
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Make sure to include these fields in the add form as well
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'password2'),
        }),
    )
    
    # Set the ordering of the users
    ordering = ('email',)

# Register the custom user model with the new admin class
admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
