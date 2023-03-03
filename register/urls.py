from django.urls import path
from rest_framework import routers

from register.views import RegistrationAPIView, UserLoginView, UserProfileView, ChangePasswordView, EditProfileView, VerificationView, SendPasswordEmailView, UserPasswordResetView

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('verify/<uid>/<token>/', VerificationView.as_view(), name='verify'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('user_profile/', UserProfileView.as_view(), name='user_profile'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('edit-profile/', EditProfileView.as_view(), name='edit-profile'),
    path('send-reset-password/', SendPasswordEmailView.as_view(), name="send-reset-password"),
    path('reset-password/', UserPasswordResetView.as_view(), name='reset-password'),
]