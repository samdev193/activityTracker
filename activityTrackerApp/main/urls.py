from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register_user"),
    path("questionnaire/", views.questionnaire, name="ask_user_questions"),
    path("profile/", views.profile, name="user_profile"),
]