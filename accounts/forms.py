from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser, Schedule


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "classes",
            "bio",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "classes",
            "bio",
        )


class CustomSchedule(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = [
            "name",
            "day",
            "start_time",
            "end_time",
        ]


class ChangeCustomSchedule:
    class Meta:
        model = Schedule
        fields = (
            "day",
            "start_time",
            "end_time",
        )


class EditCustomBio(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            "bio",
        ]
