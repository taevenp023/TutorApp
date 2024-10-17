from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

from accounts.models import CustomUser, Schedule


class HomePageView(ListView):
    model = Schedule
    template_name = "home.html"
    context_object_name = "days"
    ordering = ["start_time"]


class TutorListView(ListView):
    model = CustomUser
    template_name = "tutor_list.html"
    context_object_name = "users"
    ordering = ["first_name"]


class UserView(DetailView):
    model = CustomUser
    template_name = "tutor_page.html"
    context_object_name = "user"
