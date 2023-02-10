from django.urls import path
from .views import UserView, UserDetailView, UserReposRetrieveView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/<user_name_data>/details", UserDetailView.as_view()),
    path("users/<user_name_data>/repos", UserReposRetrieveView.as_view()),
]
