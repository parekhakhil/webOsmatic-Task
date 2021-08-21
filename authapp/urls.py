from authapp.models import UserProfile
from .views import CreateProfileView, LoginView, LogoutView, RegisterView, UserProfileView
from django.urls import path

app_name = "authapp"

urlpatterns = [
    path("signin", LoginView.as_view()),
    path("signup", RegisterView.as_view()),
    path('user/<int:pk>',UserProfileView.as_view()),
    path('user/create',CreateProfileView.as_view()),
    path('logout',LogoutView.as_view()),
]
