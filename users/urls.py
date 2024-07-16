from django.urls import path
from users import views


urlpatterns = [
    path("login/", views.loginPage, name="login")
    path("", views.profiles, name="profiles"),
    path("profiles/<str:pk>/", views.userProfile, name="user-profile"),
]