from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book


class CustomUserAdmin(UserAdmin):
    # Display email instead of username
    list_display = ("email", "date_of_birth", "is_staff")

    # Use email as the ordering field
    ordering = ("email",)

    # Extend the default fieldsets with custom fields
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )

    # Extend add_fieldsets with custom fields
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book)
