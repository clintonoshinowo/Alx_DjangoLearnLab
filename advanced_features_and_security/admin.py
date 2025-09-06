from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Import your new CustomUser model
from .models import CustomUser

# Register your CustomUser model with the admin site.
# We'll use a class that inherits from Django's built-in UserAdmin
# to customize the display.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # This list defines the columns to display in the admin list view.
    # We are using fields that actually exist on the CustomUser model
    # (inherited from AbstractUser).
    list_display = ('username', 'email', 'is_staff', 'is_active', 'date_joined')
