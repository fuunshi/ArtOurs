from django.contrib import admin
from .managers import CustomUserAdmin
from .models import CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
