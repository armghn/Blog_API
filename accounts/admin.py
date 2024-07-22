from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['email', 'username', 'name', 'is_staff']
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('name',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('name', 'email')}),)


