from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm, CustomSchedule, EditCustomBio


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class AddBioView(CreateView):
    form_class = EditCustomBio
    success_url = reverse_lazy("home")
    template_name = "edit_bio.html"


class AddAvailabilityView(CreateView):
    form_class = CustomSchedule
    success_url = reverse_lazy("home")
    template_name = "scheduling/add_availability.html"
