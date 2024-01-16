from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'is_artist')

        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)

        #     self.fields['email'].widget.attrs.update({'class': 'custom-form-input'})
        #     self.fields['username'].widget.attrs.update({'class': 'custom-form-input'})
        #     self.fields['password1'].widget.attrs.update({'class': 'custom-form-input'})
        #     self.fields['password2'].widget.attrs.update({'class': 'custom-form-input'})

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'is_artist', 'avatar', 'last_login')


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('email', 'username', 'is_artist', 'last_login')
    list_filter = ('is_artist', 'groups', 'user_permissions')
    search_fields = ('email', 'username')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'is_artist', 'avatar')}),
        ('Permissions', {'fields': ('groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )