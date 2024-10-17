from django.urls import path
from .views import SignUpView, AddAvailabilityView, AddBioView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("add_availability/", AddAvailabilityView.as_view(), name="add_availability"),
    path("edit_bio/", AddBioView.as_view(), name="add_bio"),
]
