from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # These fields will be displayed in the change form
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo',)}),
    )
    # These fields will be displayed when adding a new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.
