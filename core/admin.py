from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Artist

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Additional Information',
            {
                'fields': (
                    'is_artist',
                    'address',
                    'profile_picture',
                ),
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Artist)