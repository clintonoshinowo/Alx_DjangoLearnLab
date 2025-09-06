from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Admin configuration for the custom user model.
    """
    model = CustomUser
    list_display = ['email', 'is_staff', 'is_superuser', 'date_of_birth']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'password2', 'date_of_birth', 'profile_photo')}
         ),
    )
    search_fields = ['email']

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters by author and publication year
    list_filter = ('author', 'publication_year')
    
    # Enable search functionality on these fields
    search_fields = ('title', 'author')
# Register your models here.
