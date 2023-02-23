from rest_framework import serializers

from register.models import CustomerUser


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerUser
        fields = (
            'username',
            'full_name',
            'email',
            'password',
            'country',
            'company_name',
            'user_type',
            'phone_number',
            'corporate_number'
        )

class UserLoginSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=255)
    class Meta:
        model = CustomerUser
        fields = [
            'email',
            'password'
        ]

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerUser
        fields = [
            'full_name',
            'email',
            'country',
            'company_name',
            'user_type',
            'phone_number',
            'corporate_number',
        ]