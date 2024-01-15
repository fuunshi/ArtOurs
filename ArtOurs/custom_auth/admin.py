from django.contrib import admin
from .managers import CustomUser, CustomUserAdmin


admin.site.register(CustomUser, CustomUserAdmin)
