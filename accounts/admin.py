from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm,
    CustomSchedule,
    ChangeCustomSchedule,
)
from .models import CustomUser, Schedule


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "username",
        "first_name",
        "last_name",
        "email",
        "classes",
        "bio",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("classes", "bio")}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("classes", "bio")}),)


class CustomSchedule(admin.ModelAdmin):
    add_form = CustomSchedule
    model = Schedule
    list_display = [
        "name",
        "day",
        "start_time",
        "end_time",
    ]

    fieldsets = ((None, {"fields": ("name", "day", "start_time", "end_time")}),)
    add_fieldsets = ((None, {"fields": ("name", "day", "start_time", "end_time")}),)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Schedule, CustomSchedule)
