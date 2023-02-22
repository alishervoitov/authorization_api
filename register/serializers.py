from rest_framework import serializers

from register.models import CustomerUser


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerUser
        fields = "__all__"

class UserLoginSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=255)
    class Meta:
        model = CustomerUser
        fields = [
            'email',
            'password'
        ]