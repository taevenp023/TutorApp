from django.urls import path
from .views import HomePageView, TutorListView, UserView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("users/", TutorListView.as_view(), name="tutor_list"),
    path("users/<int:pk>/", UserView.as_view(), name="user_view"),
]
