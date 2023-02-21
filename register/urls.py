from django.urls import path
from rest_framework import routers

from register.views import RegistrationAPIView

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
]