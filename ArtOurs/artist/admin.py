from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email' , 'is_staff', 'is_artist')

    fieldsets = (
        (None, {
            "fields": (
                'username', 'password'
            ),
        }),
        ('Personal Info', {
            "fields": (
                'first_name', 'last_name', 'email', 'is_artist'
            )
        }
        ),
        ('Permissions', {
            "fields": (
                'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'
            )
        }
        ),
        ('Important Dates', {
            "fields": (
                'last_login', 'date_joined'
            )
        }
        )
    )
    

admin.site.register(User, UserAdmin)
admin.site.register(Artist)
admin.site.register(Artwork)
admin.site.register(Category)