from django.urls import path

from apps.accounts.api.views import UserProfileView, UpdateUserProfileView, MyProfileView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path("", UserProfileView.as_view()),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("me/", MyProfileView.as_view()),
    path("<int:id>", UpdateUserProfileView.as_view()),
]